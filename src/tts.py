#!/usr/bin/python3
#https://www.python.org/dev/peps/pep-0257/#handling-docstring-indentation
#https://realpython.com/documenting-python-code/
#https://www.python.org/dev/peps/pep-0008/
from gtts import gTTS
import sys
import os 
from Inputs import Inputs

def main(argv=sys.argv[1:]):
   """Text to speech
   
   Example:
      # read text
      tts.py --read="read this text"  

      # read text with speed x2
      tts.py --read="read this text" --speed="2"

      # read txt file and save to mp3:   
      tts.py -i someInputFile.txt -o someOutputFile.mp3  
   """

   def saveMp3(text="", output_file="output_file.mp3", lang='se'):
      """Save the text to read to the output_file"""
      tts = gTTS(text, lang=lang)
      print(lang)
      tts.save(output_file)
    
   def speak(output_file="output_file.mp3", speed=1):
      """Read out load the imputed text"""
      os.system(f'mpg123 --doublespeed "{speed}" ' + output_file)
      sys.exit(0)

   # First Read the input
   inputs = Inputs(args=argv)

   # Save input text to file
   if inputs.get_input_file():
        f = open(inputs.get_input_file(),"r")
        inputs.text = f.read()
        saveMp3(text=inputs.get_input_text(), output_file=inputs.get_output_file(), lang=inputs.get_lang())
        f.close()

   # Read input text out loud
   if inputs.get_speak() and inputs.get_input_text():
        saveMp3(text=inputs.get_input_text(), 
                output_file="output_file.mp3", 
                lang=inputs.get_lang()
                )
        speak(speed=inputs.get_speed(), 
              output_file="output_file.mp3"
              )

if __name__ == "__main__":
   main(sys.argv[1:])
