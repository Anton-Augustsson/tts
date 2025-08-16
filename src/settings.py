#!/usr/bin/python3
import os
import json


class Settings:

    def __init__(self, default_settings, personal_settings):
        self.__default_settings_path = default_settings
        self.__personal_settings_path = personal_settings
        self.__personal_settings = self.__read_personal_settings()

    def __read_settings(self, settings_path):
        json_file = open(settings_path, "r")
        settings = json.load(json_file)
        json_file.close()
        return settings

    def __write_file_safely(self, file_path, new_settings, mode='w'):
        dirname = os.path.dirname(str(file_path))
        os.makedirs(dirname, exist_ok=True)
    
        with open(file_path, mode) as f:
            json.dump(new_settings, f)
            f.close()

    def __read_personal_settings(self):
        if not os.path.isfile(self.__personal_settings_path):
            new_settings = self.__read_settings(self.__default_settings_path)
            self.__write_file_safely(self.__personal_settings_path, 
                                     new_settings)

        return self.__read_settings(self.__personal_settings_path)

    def __set_settings(self, key, value):
        self.__personal_settings[key] = value
        self.__write_personal_settings(self.__personal_settings)

    @property
    def speed(self):
        return round(float(self.__personal_settings['speed']), 1)

    @speed.setter
    def speed(self, value):
        self.__set_settings(key='speed', value=value)

    @property
    def lang(self):
        return self.__personal_settings['lang']

    @lang.setter
    def lang(self, value):
        self.__set_settings(key='lang', value=value)
