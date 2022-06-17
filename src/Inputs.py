#!/usr/bin/python3
import sys
import getopt
from Settings import Settings  # type: ignore
from dataclasses import dataclass


@dataclass
class Inputs:
    speed: float
    lang: str
    input_file: str
    output_file: str
    input_text: str
    speak: bool


def read_inputs(argv):
    settings = Settings()
    inputs = Inputs(speed=settings.speed,
                    lang=settings.lang,
                    input_file="",
                    output_file="",
                    input_text="",
                    speak=False)
    options = {
        "help": '-h',
        "get_speed": '-s',
        "read": ("--read"),
        "speed": ("--speed"),
        "lang": ("--lang"),
        "input": ("-i", "--ifile"),
        "output": ("-o", "--ofile"),
    }

    # Try to read the inputs
    try:
        opts, args = getopt.getopt(
            argv, "hsi:o:", ["read=", "speed=", "lang=", "ifile=", "ofile="])
    # If input could net be obtained then exit
    except getopt.GetoptError:
        print('Error run: test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    # If the inputs could be obtained interpret them
    for opt, arg in opts:
        if opt == options["help"]:
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in options["get_speed"]:
            print(inputs.speed)
        elif opt in options["read"]:
            inputs.input_text = arg  # FIXME: error if no selection.
            inputs.speak = True
        elif opt in options["speed"]:
            inputs.speed = float(arg)
            settings.speed = inputs.speed  # Update personal settings json
        elif opt in options["lang"]:
            # TODO: check if arg is a valid language
            inputs.lang = arg
            settings.lang = inputs.lang  # Update personal settings json
        elif opt in options["input"]:
            inputs.input_file = arg
        elif opt in options["output"]:
            inputs.input_file = arg

    return inputs
