#!/usr/bin/python3
# https://www.python.org/dev/peps/pep-0257/#handling-docstring-indentation
# https://realpython.com/documenting-python-code/
# https://www.python.org/dev/peps/pep-0008/
import sys
import signal
import subprocess
import pyperclip

from src.inputs import read_inputs
from src.constants import DEFAULT_SOUND_FILE_OUTPUT
from src.system_operator import pause_process, resume_process, instance_already_running, saveMp3

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
    if inputs.speak and not instance_already_running():
        windows = False
        if windows and not inputs.input_text: 
            # note that you have to ctrl-c and then run python script
            s = pyperclip.paste()
            pyperclip.copy(s)
            inputs.input_text = s
        elif not inputs.input_text:
            # With linux and mac you can just select/highlight you dont have to ctrl-c 
            print("whuy")
            cmd = "xclip -o"
            ret = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print(ret)
            inputs.input_text = ret.stdout

        input_cmd = f'{inputs.input_text}'
        lang_cmd = f'--lang {inputs.lang}'
        flag_cmd = '--nocheck'
        gtts_cmd = f'gtts-cli "{input_cmd}" {lang_cmd} {flag_cmd}'
        mpg123_cmd = f'mpg123 --doublespeed "{int(inputs.speed)}" -'
        args = [f'{gtts_cmd} | {mpg123_cmd} ']
        process = subprocess.Popen(args, shell=True)

        # Register signal handler to pause/resume process
        signal.signal(signal.SIGINT, lambda sig, frame: pause_process(process) if process.poll() is None else None)
        signal.signal(signal.SIGTSTP, lambda sig, frame: resume_process(process) if process.poll() is None else None)

        # Wait for process to complete
        process.wait()

if __name__ == "__main__":
    main(sys.argv[1:])
