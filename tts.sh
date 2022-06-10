#!/bin/bash

# If no arguments are given $HOME/Programs/tts.py is the path
if [ $# -eq 0 ] 
then
    $HOME/Programs/tts/src/tts.py --read="$(xclip -o)"
# Else if the src path
elif [ $# -eq 1 ]
then
    $HOME/Programs/tts/src/tts.py --read="$(xclip -o)" --lang="$1"
# Else if both the src path and the language is given
elif [ $# -eq 2 ]
then
    $1/tts.py --read="$(xclip -o)" --lang="$2"
else 
    echo "To many arguments was given"
fi
