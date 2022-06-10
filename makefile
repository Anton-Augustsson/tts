.PHONY: install all test clean dependencies_apt dependencies

src=./src
gnome_extensions_path=~/.local/share/gnome-shell/extensions
gnome_extension_name=tts@Anton-Augustsson.com


all: install test

help: 
	@cat ./README.md

run:
	./tts.sh

run_se:
	./tts.sh sv

test_set_speed_to_one_half:
	$(src)/DefaultSettings.py --speed=2

test_set_lang_to_sv:
	$(src)/DefaultSettings.py --lang=sv

test: test_set_speed_to_one_half test_set_lang_to_sv

requirements:
	pip install -r requirements.txt
	@echo "\n\tRequirements are ins-talled!\n"

install_gnome_extension:
	cp -r ./$(gnome_extension_name) $(gnome_extensions_path)
	@echo "\n\tGnome extension is installed!\n"

install_tts:
	chmod +x ./tts.sh $(src)/tts.py $(src)/setDefaultSettings.sh  $(src)/DefaultSettings.py $(src)/Inputs.py
	@echo "\n\ttts is now installed\n"	

install: requirements install_gnome_extension install_tts
	@echo "Now you can set up a keybinding for tts. Use $(src)/tts.sh"

clean:
	rm -r $(gnome_extensions_path)/$(gnome_extension_name)
