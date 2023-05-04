#!/usr/bin/python3
# https://www.python.org/dev/peps/pep-0257/#handling-docstring-indentation
# https://realpython.com/documenting-python-code/
# https://www.python.org/dev/peps/pep-0008/
import os
import sys
from gtts import gTTS  # type: ignore
from src.inputs import read_inputs
from src.constants import DEFAULT_SOUND_FILE_OUTPUT
import fcntl
import signal

def signal_handler(signal, frame):
    print(f'Signal {signal} received')
    #exit() 
    

def instance_already_running(label="default"):
    """
    Detect if an an instance with the label is already running, globally
    at the operating system level.

    Using `os.open` ensures that the file pointer won't be closed
    by Python's garbage collector after the function's scope is exited.

    The lock will be released when the program exits, or could be
    released if the file pointer were closed.
    """
    file_path = f"/tmp/instance_{label}.lock"
    
    # Create file if it does note exist since os.open does not do it
    with open(file_path, 'w') as f:
        f.close()

    lock_file_pointer = os.open(file_path, os.O_WRONLY)
    assert os.path.isfile(file_path)

    try:
        fcntl.lockf(lock_file_pointer, fcntl.LOCK_EX | fcntl.LOCK_NB)
        already_running = False
    except IOError:
        already_running = True

    return already_running

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

    signal.signal(signal.SIGINT, signal_handler)

    def saveMp3(text="", output_file="output_file.mp3", lang='se'):
        """
        Save the text to read to the output_file
        """
        tts = gTTS(text, lang=lang)
        print(lang)
        tts.save(output_file)

    def speak(output_file="output_file.mp3", speed=1):
        """Read out load the imputed text"""
        os.system(f'mpg123 --doublespeed "{int(speed)}" ' + output_file)
        sys.exit(0)

    # First Read the input
    inputs = read_inputs(argv)

    # Save input text to file
    if inputs.input_file:
        f = open(inputs.input_file, "r")
        saveMp3(text=inputs.input_text,
                output_file=inputs.output_file,
                lang=inputs.lang)
        f.close()

    # Read input text out loud
    if inputs.speak and inputs.input_text and not instance_already_running():
        input_cmd = f'{inputs.input_text}'
        lang_cmd = f'--lang {inputs.lang}'
        flag_cmd = '--nocheck'
        gtts_cmd = f'gtts-cli "{input_cmd}" {lang_cmd} {flag_cmd}'
        mpg123_cmd = f'mpg123 --doublespeed "{int(inputs.speed)}" -'
        os.system(f'{gtts_cmd} | {mpg123_cmd} ')

if __name__ == "__main__":
    main(sys.argv[1:])
