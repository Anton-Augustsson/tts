#!/usr/bin/python3
from gtts import gTTS
import sys, getopt
import os 

class Inputs:
   def __init__(self, args):
      self.speed       = ''
      self.input_file  = '' 
      self.output_file = ''
      self.input_text  = ''
      self.speak       = False
      self.readInput(argv=args)

   def readInput(self, argv):
      """Interpreted the inputs and save it into dictionary (inputs)"""

      # The available options to have as arguments when runing the program
      options = {
         "help": '-h',
         "read": ("--read"),
         "speed": ("--speed"),
         "input": ("-i", "--ifile"),
         "output": ("-o", "--ofile"),
      }
      
      def opt_error():
         """Prints out a help message and exit with error code"""
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit(2)

      def opt_help():
         """Print out help message and exit"""
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()

      def opt_read(arg):
         """Selects the speak option and saves the text to speak"""
         self.input_text = arg
         self.speak      = True

      def opt_speed(arg):
         """Changes the speed of the speaker"""
         self.speed = int(arg)

      def opt_input_file(arg):
         """Sets the input file"""
         self.input_file = arg

      def opt_output_file(arg):
         """Sets the output file"""
         self.output_file = arg

      # Try to read the inputs
      try:
         opts, args = getopt.getopt(argv,"hi:o:",["read=","speed=","ifile=","ofile="])
      # If input could net be obtained then exit
      except getopt.GetoptError:
         opt_error()
      # If the inputs could be obtained interpret them
      for opt, arg in opts:
         if opt == options["help"]:     opt_help()
         elif opt in options["read"]:   opt_read(arg) 
         elif opt in options["speed"]:  opt_speed(arg) 
         elif opt in options["input"]:  opt_input_file(arg)
         elif opt in options["output"]: opt_output_file(arg)

   def get_input_text(self):  return self.input_text
   def get_input_file(self):  return self.input_file
   def get_output_file(self): return self.output_file
   def get_speed(self):       return self.speed
   def get_speak(self):       return self.speak


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

   def saveMp3(text="", output_file="output_file.mp3"):
      """Save the text to read to the output_file"""
      tts = gTTS(text)
      print(output_file)
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
        saveMp3(text=inputs.get_input_text(), output_file=inputs.get_output_file())
        f.close()

   # Read input text out loud
   if inputs.get_speak() and inputs.get_input_text():
        saveMp3(text=inputs.get_input_text(), output_file="output_file.mp3")
        speak(speed=inputs.get_speed(), output_file="output_file.mp3")


if __name__ == "__main__":
   main(sys.argv[1:])