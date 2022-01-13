#!/bin/bash

# If no arguments are given $HOME/Programs/tts.py is the path
if [ $# -eq 1 ] 
then
    $HOME/Programs/tts/DefaultSettings.py $1 #TODO: don't hardcode
# Else the first argument creates the path $HOME/$1/tts.py
else
    $HOME/$2/DefaultSettings.py $1 #TODO: don't hardcode 
fi

