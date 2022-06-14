#!/usr/bin/python3
import os
import sys
import json
import getopt


class Settings:

    def __init__(self, args=None):
        dirname = os.path.dirname(os.path.realpath(__file__))
        self.__default_settings_path = dirname + "/defaultSettings.json"
        self.__personal_settings_path = dirname + "/personalSettings.json"
        self.__personal_settings = self.__read_personal_settings()

        if args:
            self.__read_input(argv=args)

    def __read_input(self, argv):
        try:
            opts, args = getopt.getopt(argv, "h:", ["speed=", "lang="])
        except getopt.GetoptError:
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-h':
                print('to be added ')
                sys.exit()
            elif opt in "--speed":
                self.speed = arg
            elif opt in "--lang":
                self.lang = arg

    def __read_settings(self, settings_path):
        json_file = open(settings_path, "r")
        settings = json.load(json_file)
        json_file.close()
        return settings

    def __create_personal_settings(self):
        default_settings = self.__read_settings(self.__default_settings_path)
        self.__write_personal_settings(default_settings)

    def __read_personal_settings(self):
        if not os.path.exists(self.__personal_settings_path):
            self.__create_personal_settings()

        return self.__read_settings(self.__personal_settings_path)

    def __write_personal_settings(self, new_settings):
        json_file = open(self.__personal_settings_path, "w")
        json.dump(new_settings, json_file)
        json_file.close()

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


if __name__ == "__main__":
    Settings(sys.argv[1:])
