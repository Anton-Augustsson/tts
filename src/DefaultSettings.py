import json
from os import write
import sys, getopt

class DefaultSettings:
    def __init__(self):
        self.file_path = "src/defaultSettings.json"
        self.default_settings = self.read_default_settings()
        
    def read_default_settings(self):
        f_r = open(self.file_path, "r") #FIXME: dynamicly find the path
        json_prev = json.load(f_r)
        f_r.close()
        return json_prev

    def write_default_settings(self, json_new):
        f_w = open(self.file_path, "w")
        json.dump(json_new, f_w)
        f_w.close()

    def set_speed(self, value):
        self.default_settings['speed'] = value
        self.write_default_settings(self.default_settings)

if __name__ == "__main__":
   d = DefaultSettings()
   d.set_speed(sys.argv[1]) #TODO: don't hard code the index


