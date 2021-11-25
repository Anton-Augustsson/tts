#!/bin/bash

# Install nessesary dependencies and configure for popos
install_popos(){
    echo "Installing dependencies for popos"

    # Install pip
    sudo apt update
    sudo apt install python3-pip

    # Install python packages
    pip install gTTS
}

# Call the install function
install_popos
