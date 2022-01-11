/* extension.js
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * SPDX-License-Identifier: GPL-2.0-or-later
 */

/* exported init */

//https://wiki.gnome.org/Projects/GnomeShell/Extensions/EcoDoc/Applet
const St = imports.gi.St;
const Gio = imports.gi.Gio;

const ExtensionUtils = imports.misc.extensionUtils;
const Me = ExtensionUtils.getCurrentExtension();
const Main = imports.ui.main;
const PanelMenu = imports.ui.panelMenu;
//import { PopupMenuExample } from './popup.js';
const PopupMenu = imports.ui.popupMenu;
const Slider = imports.ui.slider

const Lang = imports.lang;


const HelloWorld_Indicator = new Lang.Class({
    Name: 'HelloWorld.indicator',
    Extends: PanelMenu.Button   ,

    _init: function(){
        this.parent(0.0);

        // Add an icon
        let icon = new St.Icon({
            gicon: new Gio.ThemedIcon({name: 'face-laugh-symbolic'}),
            style_class: 'system-status-icon'
        });
	

        this.actor.add_child(icon);
        
        let menuItem = new PopupMenu.PopupMenuItem('Play/Pause');
        menuItem.actor.connect('button-press-event', function(){ Main.notify('Example Notification', 'Hello World !') });
        //menuItem.actor.connect('button-press-event', function(){ Main.notify('Change play speed') });

        //let switchItem = new PopupMenu.PopupSwitchMenuItem("hello world");

        this.menu.addMenuItem(menuItem);

        // We create our slider for the Panel AggregateMenu
        this._item = new PopupMenu.PopupBaseMenuItem({activate: false});
        this.menu.addMenuItem(this._item);

        // Create the slider
        this._slider = new Slider.Slider(0);
        //this._sliderChangedId = this._slider.connect('notify::value',
        //    this._sliderChanged.bind(this));
        //this._slider.accessible_name = _('Night Light Temperature');

        //this._slider_icon = new St.Icon({icon_name: 'night-light-symbolic',
        //    style_class: 'popup-menu-icon'});

        // Add the slider & its icon to the base menu
        //this._item.add(this._slider_icon);
        this._item.add_child(this._slider);
        //this.menu.addMenuItem(switchItem);
        //this.menu.addMenuItem(sliderItem);
    }
});

/* Global variables for use as button to click */

class Extension {
    constructor() {
        this._indicator = null;
    }
    
    enable() {
        log(`enabling ${Me.metadata.name}`);

        let indicatorName = `${Me.metadata.name} Indicator`;
        
	    // Create button
	    //button = new PopupMenuExample;
        let _indicator =  new HelloWorld_Indicator();
        Main.panel._addToPanelBox('HelloWorld', _indicator, 1, Main.panel._rightBox);

        // `Main.panel` is the actual panel you see at the top of the screen,
        // not a class constructor.
        //Main.panel.addToStatusArea(indicatorName, this._indicator);
	//Main.panel.addToStatusArea('PopupMenuExample', button, 0, 'right');
    }
    
    // REMINDER: It's required for extensions to clean up after themselves when
    // they are disabled. This is required for approval during review!
    disable() {
        log(`disabling ${Me.metadata.name}`);

        _indicator.destroy();   
        this._indicator.destroy();
        this._indicator = null;

	// Remove button that is created when enableing the extension
	//button.destroy();
    }
}


function init() {
    log(`initializing ${Me.metadata.name}`);
    return new Extension();
}

