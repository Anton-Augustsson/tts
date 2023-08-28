# AATTS
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Contribution guidelines for this project](docs/CONTRIBUTING.md)

`aatts` is a text to speech program used for speech synthesis as well as generate a mp3 from a text file.

## Dependencies
The following dependencies are needed in order to install and run the program.
- `python3`
- `pip`
- `mpg123`
- `xclip`

See `requirements.txt` for python dependencies.

## Installation
Currently, only linux is supported, preferably with gnome, but not required to run `aatts` just allowed the usage of gnome extension. 

Run `make install` to install the program. 

### Windows installation
```
pyinstaller  --onefile --noconsole main.py
```
Note: If you can not run this command even though pyinstaller is installed you can call the pyinstaller exec file directly. It should be located in `C:\Users\<Your username>\AppData\Local\Packages\PythonSoftwareFoundation.<Your Python version>\LocalCache\local-packages\<Your Python version>\Scripts\pyinstaller.exe`

This will generate an executable file in the dist directory. Then Right-click -> new -> shortcut. Put the shortcut in the desktop directory. Then create a keybinding to run that shortcut by right-clicking the shortcut and writing your desired keyboard shortcut.


## Gnome extension
![image](img/gnome-extension.png)

The gnome extension will automatically be installed when ruining `make install`.

## Usage
The currently selected text can be determine with `xclip -o`. This command can be used to then 
read the currently selected text.

``` bash
aatts --read="$(xclip -o)"
```

It is also possible to the speed and language.

``` bash
aats --speed=1.4 --lang="en"
```

