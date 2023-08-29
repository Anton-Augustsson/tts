import os
from src.enums import OperatingSystem 


def get_data_path(operating_system):
    if operating_system == OperatingSystem.LINUX:
        return os.path.join(os.path.expanduser('~'), "/usr/share/aatts")
    elif operating_system == OperatingSystem.WINDOWS:
        return os.path.join(os.environ['ProgramData'], "aatts")
    elif operating_system == OperatingSystem.MAC:
        return os.path.join(os.path.expanduser('~'), "/usr/share/aatts")


def get_sound_file_output_path(operating_system):
    data_path = get_data_path(operating_system)
    return os.path.join(data_path, "outputfile.mp3")


def get_settings_path(operating_system):
    data_path = get_data_path(operating_system)
    default_settings = os.path.join(data_path, "defaultSettings.json")
    personal_settings = os.path.join(data_path, "personalSettings.json")
    return (default_settings, personal_settings)
