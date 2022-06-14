##
# Python scripts
#
# @file
# @version 0.1
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

test: 
	python3 -m pytest

requirements:
	pip install -r requirements.txt
	@echo "\n\tRequirements are ins-talled!\n"

yapf:
	python3 -m yapf --recursive --in-place .

flake:
	python3 -m flake8

mypy:
	python3 -m mypy src

format: yapf flake mypy

install_gnome_extension:
	cp -r ./$(gnome_extension_name) $(gnome_extensions_path)
	@echo "\n\tGnome extension is installed!\n"

install_tts:
	chmod +x ./tts.sh $(src)/tts.py $(src)/Settings.py $(src)/Inputs.py
	@echo "\n\ttts is now installed\n"	

install: requirements install_gnome_extension install_tts
	@echo "Now you can set up a keybinding for tts. Use $(src)/tts.sh"

clean:
	rm -r $(gnome_extensions_path)/$(gnome_extension_name)
