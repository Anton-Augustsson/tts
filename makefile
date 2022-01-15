.PHONY: install all test clean

script_dir=scripts
install_script_path=$(script_dir)/install.sh

all:
	echo "Hello"


help: 
	echo "Help"

run:
	src/tts.sh Documents/tts/src

run_se:
	src/tts.sh Documents/tts/src sv

test: test_set_speed_to_one_half test_set_lang_to_sv

test_set_speed_to_one_half:
	src/setDefaultSettings.sh 2 Documents/tts/src

test_set_lang_to_sv:
	src/setDefaultSettings.sh sv Documents/tts/src

install:
	chmod +x $(install_script_path)
	$(install_script_path)
