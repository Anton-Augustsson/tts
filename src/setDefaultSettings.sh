#!/bin/bash

# If no arguments are given $HOME/Programs/tts.py is the path
if [ $# -eq 1 ] 
then
    $HOME/Programs/tts/DefaultSettings.py $1 #TODO: don't hardcode
# Else the first argument creates the path $HOME/$1/tts.py
elif [ $# -eq 2 ] 
then 
    $2/DefaultSettings.py $1 #TODO: don't hardcode 
else
    echo "language and or path was not given"
fi

