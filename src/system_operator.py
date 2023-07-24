import os
import fcntl
import signal
from gtts import gTTS  # type: ignore

def pause_process(process):
    process.send_signal(signal.SIGSTOP)

def resume_process(process):
    process.send_signal(signal.SIGCONT)

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

def saveMp3(text="", output_file="output_file.mp3", lang='se'):
    """
    Save the text to read to the output_file
    """
    tts = gTTS(text, lang=lang)
    print(lang)
    tts.save(output_file)

