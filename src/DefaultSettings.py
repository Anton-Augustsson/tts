#!/usr/bin/python3
import json
import sys, getopt
import os

class DefaultSettings:

    def __init__(self, args=None):
        file_dir  = os.path.dirname(os.path.realpath(__file__)) 
        file_name = "/defaultSettings.json"
        self.file_path = file_dir + file_name
        self.default_settings = self.read_default_settings()

        if __name__ == "__main__":
            self.read_input(argv=args)
        
    def read_input(self, argv):
        try:
            opts, args = getopt.getopt(argv,"h:",["speed=","lang="])
        except getopt.GetoptError:
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-h': 
                print('to be added ')
                sys.exit()
            elif opt in "--speed": 
                self.set_speed(value=arg)
            elif opt in "--lang":
                self.set_lang(value=arg)

    def read_default_settings(self):
        f_r = open(self.file_path, "r") #FIXME: dynamicly find the path
        json_prev = json.load(f_r)
        f_r.close()
        return json_prev

    def write_default_settings(self, json_new):
        f_w = open(self.file_path, "w")
        json.dump(json_new, f_w)
        f_w.close()

    def set(self, key, value):
        self.default_settings[key] = value
        self.write_default_settings(self.default_settings)

    def set_speed(self, value):
        self.set(key='speed', value=value)

    def set_lang(self, value):
        self.set(key='lang', value=value)

    def get_speed(self):
        return round(float(self.default_settings['speed']), 1)

    def get_lang(self):
        return self.default_settings['lang']


if __name__ == "__main__":
    DefaultSettings(sys.argv[1:])
