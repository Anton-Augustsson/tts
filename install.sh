#!/bin/bash
selectDesktopEnviroment(){
    echo "\n\n Which desktop enviroment do you want to install?"

    # Operating system names are used here as a data source
    select de in dwm bspwm none
    do

    case $de in
    "dwm")
    echo "you have selected $de."
    break
    ;;
    "bspwm")
    echo "you have selected $de."
    break
    ;;
    "none")
    echo "No desktop enviroment will be installed"
    break
    ;;
    # Matching with invalid data
    *)
    echo "Invalid entry."
    ;;
    esac
    done
}


selectDesktopEnviroment
