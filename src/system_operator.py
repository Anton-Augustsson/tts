import os
import sys
import fcntl
import signal
import subprocess
import pyperclip # Write in requirements
import pygame # Write in requirements
from gtts import gTTS  # type: ignore
from src.enums import OperatingSystem 

def get_os():
    if sys.platform.startswith('linux'):
        return OperatingSystem.LINUX
    elif sys.platform.startswith('win'):
        return OperatingSystem.WINDOWS
    elif sys.platform.startswith('darwin'):
        return OperatingSystem.MAC
    else:
        return 'unknown'

def pause_process(process):
    process.send_signal(signal.SIGSTOP)

def resume_process(process):
    process.send_signal(signal.SIGCONT)

def instance_already_running_linux(label="default"):
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

def instance_already_running_windows(label="default"):
    # TODO:
    return False 

def instance_already_running(operating_system=OperatingSystem.LINUX):
    """
    Detect if an an instance with the label is already running, globally
    at the operating system level.

    Using `os.open` ensures that the file pointer won't be closed
    by Python's garbage collector after the function's scope is exited.

    The lock will be released when the program exits, or could be
    released if the file pointer were closed.
    """
    if operating_system == OperatingSystem.LINUX:
        return instance_already_running_linux()
    elif operating_system == OperatingSystem.WINDOWS:
        return instance_already_running_windows()
    elif operating_system == OperatingSystem.MAC:
        return False 

def save_mp3(text="", output_file="output_file.mp3", lang='se'):
    """
    Save the text to read to the output_file
    """
    tts = gTTS(text, lang=lang)
    print(lang)
    tts.save(output_file)

def read_clipboard_linux():
    # With linux and mac you can just select/highlight you dont have to ctrl-c 
    cmd = "xclip -o"
    ret = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return ret.stdout

def read_clipboard_windows():
    s = pyperclip.paste()
    pyperclip.copy(s)
    return s

def read_clipboard(operating_system=OperatingSystem.LINUX):
    if operating_system == OperatingSystem.LINUX:
        return read_clipboard_linux()
    elif operating_system == OperatingSystem.WINDOWS:
        return read_clipboard_windows()
    elif operating_system == OperatingSystem.MAC:
        return False 
    return "TODO"

def speak_linux(input):
    """
    read text out loud
    """
    input_cmd = f'{input.input_text}'
    lang_cmd = f'--lang {input.lang}'
    flag_cmd = '--nocheck'
    gtts_cmd = f'gtts-cli "{input_cmd}" {lang_cmd} {flag_cmd}'
    mpg123_cmd = f'mpg123 --doublespeed "{int(input.speed)}" -'
    args = [f'{gtts_cmd} | {mpg123_cmd} ']
    process = subprocess.Popen(args, shell=True)

    # Register signal handler to pause/resume process
    signal.signal(signal.SIGINT, lambda sig, frame: pause_process(process) if process.poll() is None else None)
    signal.signal(signal.SIGTSTP, lambda sig, frame: resume_process(process) if process.poll() is None else None)

    # Wait for process to complete
    process.wait()

def speak_windows(input):
    # TODO: make a process instead
    save_mp3(text=input.input_text,
             output_file=input.output_file,
             lang=input.lang)

    # Initialize pygame mixer
    pygame.mixer.init()
    # Load the audio file
    pygame.mixer.music.load(input.output_file)
    # Play the audio
    pygame.mixer.music.play()
    # Wait for the playback to finish
    while pygame.mixer.music.get_busy():
        continue

def speak(input, operating_system=OperatingSystem.LINUX):
    if operating_system == OperatingSystem.LINUX:
        return speak_linux(input)
    elif operating_system == OperatingSystem.WINDOWS:
        return speak_windows(input)
    elif operating_system == OperatingSystem.MAC:
        return False 

