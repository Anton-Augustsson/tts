#!/usr/bin/python3
# https://www.python.org/dev/peps/pep-0257/#handling-docstring-indentation
# https://realpython.com/documenting-python-code/
# https://www.python.org/dev/peps/pep-0008/
import sys
from src.inputs import read_inputs
from src.system_operator import instance_already_running, save_mp3, get_os, read_clipboard, speak

def main(argv=sys.argv[1:]):
    """
    Text to speech

    Example:
      # read text
      tts.py --read="read this text"

      # read text with speed x2
      tts.py --read="read this text" --speed="2"

      # read txt file and save to mp3:
      tts.py -i someInputFile.txt -o someOutputFile.mp3
    """

    # Read the input and save it into a input model
    inputs = read_inputs(argv)
    operating_system = get_os()

    # Decide if speaking or just saving to file
    if inputs.speak and not instance_already_running(operating_system):
        # If speaking then look if there is any text to speak
        # otherwise read from clipboard
        if not inputs.input_text:
            inputs.input_text = read_clipboard(operating_system)
        # Read input text out loud
        speak(inputs, operating_system)
    elif not inputs.speak and inputs.input_file:
        # Save input text to file
        save_mp3(text=inputs.input_text,
                output_file=inputs.output_file,
                lang=inputs.lang)

if __name__ == "__main__":
    main(sys.argv[1:])
