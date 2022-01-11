//https://github.com/julio641742/gnome-shell-extension-reference/blob/master/tutorials/POPUPMENU-EXTENSION.md
//
/* Import St because is the library that allow you to create UI elements */
const St = imports.gi.St;


/* Import Clutter because is the library that allow you to layout UI elements */
const Clutter = imports.gi.Clutter;

/*
Import Main because is the instance of the class that have all the UI elements
and we have to add to the Main instance our UI elements
*/
const Main = imports.ui.main;

/*
Import PanelMenu and PopupMenu 
See more info about these objects in REFERENCE.md
*/
const PanelMenu = imports.ui.panelMenu;
const PopupMenu = imports.ui.popupMenu;

/*
Import Lang because we will write code in a Object Oriented Manner
*/
const Lang = imports.lang;

/*
In here we are creating a new Class named `PopupMenuExample`, it is derivated from `panelMenu.Button`
If you analize the class, you can see that:
	`Name:` is the same as the name class
	`Extends:` is the class you are extending from
	`_init: function(){}` is the constructor
	-destroy: function{}` is the destructor
	and you can add more functions to this class if you want to
*/
export const PopupMenuExample = new Lang.Class({
	Name: 'PopupMenuExample',	// Class Name
	Extends: PanelMenu.Button,	// Parent Class

	// Constructor
	_init: function() {
		/* 
		This is calling the parent constructor
		1 is the menu alignment (1 is left, 0 is right, 0.5 is centered)
		`PopupMenuExample` is the name
		true if you want to create a menu automatically, otherwise false
		*/
		this.parent(1, 'PopupMenuExample', false);

		// We are creating a box layout with shell toolkit
		let box = new St.BoxLayout();

		/*
		A new icon 'system-search-symbolic'.symbolic
		All icons are found in `/usr/share/icons/theme-being-used`
		In other tutorials we will teach you how to use your own icons

		The class 'system-status-icon` is very useful, remove it and restart the shell then you will see why it is useful here
		*/
		let icon =  new St.Icon({ icon_name: 'system-search-symbolic', style_class: 'system-status-icon'});

		// A label expanded and center aligned in the y-axis
		let toplabel = new St.Label({ text: ' Menu ',
			y_expand: true,
			y_align: Clutter.ActorAlign.CENTER });

		// We add the icon, the label and a arrow icon to the box
		box.add(icon);
		box.add(toplabel);
		box.add(PopupMenu.arrowIcon(St.Side.BOTTOM));

		// We add the box to the button
		// It will be showed in the Top Panel
		this.actor.add_child(box);

		// This is an example of PopupSubMenuMenuItem, a menu expander
		let popupMenuExpander = new PopupMenu.PopupSubMenuMenuItem('PopupSubMenuMenuItem');

		// This is an example of PopupMenuItem, a menu item. We will use this to add as a submenu
		let submenu = new PopupMenu.PopupMenuItem('PopupMenuItem');

		// A new label
		let label = new St.Label({text:'Item 1'});

		// Add the label and submenu to the menu expander
		popupMenuExpander.menu.addMenuItem(submenu);
		popupMenuExpander.menu.box.add(label);
		
		// The CSS from our file is automatically imported
		// You can add custom styles like this
		// REMOVE THIS AND SEE WHAT HAPPENS
		popupMenuExpander.menu.box.style_class = 'PopupSubMenuMenuItemStyle';
		
		// Other standard menu items
		let menuitem = new PopupMenu.PopupMenuItem('PopupMenuItem');
		let switchmenuitem = new PopupMenu.PopupSwitchMenuItem('PopupSwitchMenuItem');
		let imagemenuitem = new PopupMenu.PopupImageMenuItem('PopupImageMenuItem', 'system-search-symbolic');		

		// Assemble all menu items
		this.menu.addMenuItem(popupMenuExpander);
		// This is a menu separator
		this.menu.addMenuItem(new PopupMenu.PopupSeparatorMenuItem());
		this.menu.addMenuItem(menuitem);
		this.menu.addMenuItem(new PopupMenu.PopupSeparatorMenuItem());
		this.menu.addMenuItem(switchmenuitem);
		this.menu.addMenuItem(new PopupMenu.PopupSeparatorMenuItem());
		this.menu.addMenuItem(imagemenuitem);


/*
The following three object.connect(`signal`, Lang.bind(this, callback) are special functions
`signal`: there are many signals, you will see more in other tutorials
Lang.bin(this, callback): You will always need to include this
	callback is the function being called when `signal` is fired
		by default the first paramenter is the object that fired the signal
*/
		/*
		With PopupSwitchMenuItem you can use the signal `toggled` and do interesting stuff with it
		- function(object, value)
			object is the object sending the signal
			value is either true or false, depending on the switch
		*/
		switchmenuitem.connect('toggled', Lang.bind(this, function(object, value){
			// We will just change the text content of the label
			if(value) {
				label.set_text('On');
			} else {
				label.set_text('Off');
			}
		}));

		/*
		With Popup*MenuItem you can use the signal `activate`, it is fired when the user clicks over a menu item
		*/
		imagemenuitem.connect('activate', Lang.bind(this, function(){
			toplabel.set_text('Changed');
		}));

		/*
		With 'open-state-changed' on a popupmenu we can know if the menu is being shown
		We will just show the submenu menu items automatically, (by default it is not shown)
		*/
		this.menu.connect('open-state-changed', Lang.bind(this, function(){
			popupMenuExpander.setSubmenuShown(true);
		}));

	},

	/*
	We destroy the button
	*/
	destroy: function() {
		/*
		This call the parent destroy function
		*/
		this.parent();
	}
});
