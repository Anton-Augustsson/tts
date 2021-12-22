.PHONY: install all test clean

script_dir=scripts
install_script_path=$(script_dir)/install.sh

all:
	echo "Hello"


help: 
	echo "Help"

run:
	src/tts.sh Documents/tts/src

install:
	chmod +x $(install_script_path)
	$(install_script_path)
