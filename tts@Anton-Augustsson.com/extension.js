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
const St  = imports.gi.St;
const Gio = imports.gi.Gio;
const GLib = imports.gi.GLib;
const ExtensionUtils = imports.misc.extensionUtils;
const Util           = imports.misc.util;
const Main      = imports.ui.main;
const PanelMenu = imports.ui.panelMenu;
const PopupMenu = imports.ui.popupMenu;
const Slider    = imports.ui.slider
const Me = ExtensionUtils.getCurrentExtension();
const Lang = imports.lang;

const PathHome  = '/home/anton' // Don't hardcode path
const PathToTts = PathHome + '/Programs/tts/main.py' // Don't hardcode

const HelloWorld_Indicator = new Lang.Class({
    Name: 'HelloWorld.indicator',
    Extends: PanelMenu.Button   ,

    _init: function(){
        this.parent(0.0);

        // Add an icon to display for Panel menu
        let icon = new St.Icon({
            gicon: new Gio.ThemedIcon({name: 'face-cool-symbolic'}),
            style_class: 'system-status-icon'
        });
        this.actor.add_child(icon);

        // Play/pause menu button
        let playPauseItem = new PopupMenu.PopupMenuItem('Play/Pause');
	let textToRead;
	playPauseItem.connect('activate', () => {
	    log('play/pause')
	    textToRead = GLib.spawn_command_line_sync("xclip -o");
	    Util.spawn([PathToTts, "--read="+textToRead[1]])
	});
        this.menu.addMenuItem(playPauseItem);

        // Select langue
	let langItems = new PopupMenu.PopupSubMenuMenuItem('Language');
	this.menu.addMenuItem(langItems);
        let sv = new PopupMenu.PopupMenuItem('');
        let en = new PopupMenu.PopupMenuItem('');
	let selectedText = "* ";
	let svDefaultText = "sv";
	let enDefaultText = "en";
	let svLabel = new St.Label({text: svDefaultText});
	let enLabel = new St.Label({text: enDefaultText});

	sv.add_child( svLabel );
	en.add_child( enLabel );

	sv.connect('activate', () => {
	    log('language selected: sv');
	    Util.spawn([PathToTts, '--lang=sv']);
	    svLabel.text = selectedText + svDefaultText
	    enLabel.text = enDefaultText
	});
	en.connect('activate', () => {
	    log('language selected: en');
	    Util.spawn([PathToTts, '--lang=en']);
	    svLabel.text = svDefaultText
	    enLabel.text = selectedText + enDefaultText
	});
	
	langItems.menu.addMenuItem( sv );
	langItems.menu.addMenuItem( en, 0 );

        // Create slider component
        this._item = new PopupMenu.PopupBaseMenuItem({activate: false});
        this.menu.addMenuItem(this._item);

        // Label for slider
        let slider_label = new St.Label({ text: "Speed: " });
        this._item.add_child(slider_label);

        // Create the slider itself
	let maxSpeed = 2
	let minSpeed = 1

	let getSpeedCommand = `${PathToTts} -s`
	let [, settingsSpeed] = GLib.spawn_command_line_sync(getSpeedCommand);
	let sliderPosition = settingsSpeed - minSpeed
        log(`speed ${settingsSpeed}`);
        log(`position of slider ${sliderPosition}`);

        this._slider = new Slider.Slider(sliderPosition);
        this._slider.accessible_name = _('Night Light Temperature');
        this._sliderChangedId   = this._slider.connect('notify::value', () => {
            let sliderValue     = this._slider.value;
            let playSpeedString = String( sliderValue + minSpeed )
            Util.spawn([PathToTts, '--speed=' + playSpeedString])
        });

        this._item.add_child(this._slider);


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

