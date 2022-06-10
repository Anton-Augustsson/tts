#!/bin/bash
install_tts(){
    
	FILE_PATH_APT=(which apt-get)	
	FILE_PATH_YUM=(which yum)	
    	if [ -a $FILE_PATH ]
    	then
		sudo apt update
		sudo apt install python3-pip

		pip install 
	elif [ -a $FILE_PATH_YUM ]
    	then
     		echo "yum"
	else
		echo "no package manager was found"
    	fi
}

# Call the install function
install_tts
