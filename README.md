# AATTS
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Contribution guidelines for this project](docs/CONTRIBUTING.md)

`aatts` is a text to speech program used for speech synthesis as well as generate a mp3 from a text file.

## Dependencies
The following dependencies are needed in order to install and run the program.
- `mpg123`
- `xclip`


## Installation
Currently, only linux is supported, preferably with gnome, but not required to run `aatts` just allowed the usage of gnome extension. 

Run `make install` to install the program. 

### Windows installation
Create a bat file
```
@echo off
start "" "C:\path\to\your\tool.exe"
```
This will generate an executable file in the dist directory. Then Right-click -> new -> shortcut. Put the shortcut in the desktop directory. Then create a keybinding to run that shortcut by right-clicking the shortcut and writing your desired keyboard shortcut.


## Usage
The currently selected text can be determine with `xclip -o`. This command can be used to then 
read the currently selected text.

``` bash
aatts --read="$(xclip -o)"
```

It is also possible to the speed and language.

``` bash
aatts --speed=1.4 --lang="en"
```

