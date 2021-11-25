#!/bin/bash
install_tts(){
    root_dir=scripts
    os_install_scripts_dir=$root_dir/os_install_scripts
    intsall_popos_path=$os_install_scripts_dir/install_popos.sh
    intsall_ubuntu_path=$os_install_scripts_dir/install_ubuntu.sh

    echo "\n\n Which desktop enviroment do you want to install?"

    # Propt for choosing a operating to install
    select operating_system in popos ubuntu none
    do

    case $operating_system in
	"popos")
    		echo "you have selected $operating_system."
		chmod +x $intsall_popos_path
		$intsall_popos_path
    		break
    	;;
    	"ubuntu")
    		echo "you have selected $operating_system."
		chmod +x $intsall_ubuntu_path
		$intsall_ubuntu_path
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

# Call the install function
install_tts
