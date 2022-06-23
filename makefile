##
# Python scripts
#
# @file
# @version 0.1
.PHONY: install all test clean

src=./src
gnome_extensions_path=~/.local/share/gnome-shell/extensions
gnome_extension_name=tts@Anton-Augustsson.com
system_highlighted_text=$(shell xclip -o) 
program_name=aatts

all: install test

help: 
	@cat ./README.md

run:
	./main.py --read="$(system_highlighted_text)"

run_en:
	./main.py --read="$(system_highlighted_text)" --lang="en"

run_se:
	./main.py --read="$(system_highlighted_text)" --lang="sv"

test: 
	python3 -m pytest

debug_gnome_extension:
	journalctl -f -o cat /usr/bin/gnome-shell

requirements:
	pip install -r requirements.txt
	@echo "\n\tRequirements are installed!\n"

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
	cp -r ./data ~/.local/share/$(program_name)
	pyinstaller --onefile main.py
	cp ./dist/main ~/.local/bin/$(program_name)
	@echo "\n\ttts is now installed\n"	

install: requirements install_gnome_extension install_tts
	@echo "Now you can set up a keybinding for tts. Use $(src)/tts.sh"

clean:
	rm -r ~/.local/share/$(program_name)
	rm ~/.local/bin/$(program_name)
	rm -r $(gnome_extensions_path)/$(gnome_extension_name)
