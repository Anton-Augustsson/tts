import os

# TODO: refactor could have a type containing 3 values for linux, mac, and windows
DATA_PATH = os.path.join(os.path.expanduser('~'), "/usr/share/aatts")
#DATA_PATH_WINDOWS = os.path.join(os.environ['ProgramData'], "aatts") # TODO: test

DEFAULT_SETTINGS = os.path.join(DATA_PATH, "defaultSettings.json")
#DEFAULT_SETTINGS_WINDOWS = os.path.join(DATA_PATH_WINDOWS, "defaultSettings.json")

PERSONAL_SETTINGS = os.path.join(DATA_PATH, "personalSettings.json")
#PERSONAL_SETTINGS_WINDOWS = os.path.join(DATA_PATH_WINDOWS, "personalSettings.json")

DEFAULT_SOUND_FILE_OUTPUT = os.path.join(DATA_PATH, "outputfile.mp3")
#DEFAULT_SOUND_FILE_OUTPUT = os.path.join(DATA_PATH, "outputfile.mp3")
