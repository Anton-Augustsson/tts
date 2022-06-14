#!/usr/bin/python3
import sys
import getopt
from src.Settings import Settings


class Inputs:

    def __init__(self, args=None):
        settings = Settings()
        self.speed = settings.speed
        self.input_file = ""
        self.output_file = ""
        self.input_text = ""
        self.speak = False
        self.lang = settings.lang

        self.readInput(argv=args)

    def readInput(self, argv):
        """Interpreted the inputs and save it into dictionary (inputs)"""

        # The available options to have as arguments when runing the program
        options = {
            "help": '-h',
            "read": ("--read"),
            "speed": ("--speed"),
            "lang": ("--lang"),
            "input": ("-i", "--ifile"),
            "output": ("-o", "--ofile"),
        }

        def opt_error():
            """Prints out a help message and exit with error code"""
            print('Error run: test.py -i <inputfile> -o <outputfile>')
            sys.exit(2)

        def opt_help():
            """Print out help message and exit"""
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()

        def opt_read(arg):
            """Selects the speak option and saves the text to speak"""
            self.input_text = arg  # FIXME: error if no selection.
            self.speak = True

        def opt_speed(arg):
            """Changes the speed of the speaker"""
            self.speed = float(arg)

        def opt_lang(arg):
            """Changes the language of the speaker"""
            self.lang = arg

        def opt_input_file(arg):
            """Sets the input file"""
            self.input_file = arg

        def opt_output_file(arg):
            """Sets the output file"""
            self.output_file = arg

        # Try to read the inputs
        try:
            opts, args = getopt.getopt(
                argv, "hi:o:",
                ["read=", "speed=", "lang=", "ifile=", "ofile="])
        # If input could net be obtained then exit
        except getopt.GetoptError:
            opt_error()
        # If the inputs could be obtained interpret them
        for opt, arg in opts:
            if opt == options["help"]:
                opt_help()
            elif opt in options["read"]:
                opt_read(arg)
            elif opt in options["speed"]:
                opt_speed(arg)
            elif opt in options["lang"]:
                opt_lang(arg)
            elif opt in options["input"]:
                opt_input_file(arg)
            elif opt in options["output"]:
                opt_output_file(arg)

    def get_input_text(self):
        return self.input_text

    def get_input_file(self):
        return self.input_file

    def get_output_file(self):
        return self.output_file

    def get_speed(self):
        return self.speed

    def get_speak(self):
        return self.speak

    def get_lang(self):
        return self.lang


if __name__ == "__main__":
    Inputs(sys.argv[1:])
