#!/bin/bash

# If no arguments are given $HOME/Programs/tts.py is the path
if [ $# -eq 0 ] 
then
    $HOME/Programs/tts.py --read="$(xclip -o)"
# Else the first argument creates the path $HOME/$1/tts.py
else
    $HOME/$1/tts.py --read="$(xclip -o)"
fi

