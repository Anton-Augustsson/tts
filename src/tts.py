#!/usr/bin/python3
from gtts import gTTS
import sys, getopt
import os 

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

   inputs = {
      "input_file": '',
      "output_file": '',
      "input_text": '',
      "speed": 1,
      "speak": False 
   }

   def saveMp3(text="", output_file="output_file.mp3"):
      """Save the text to read to the output_file"""
      tts = gTTS(text)
      print(output_file)
      tts.save(output_file)
    
   def speak(output_file="output_file.mp3", speed=1):
      """Read out load the imputed text"""
      os.system(f'mpg123 --doublespeed "{speed}" ' + output_file)
      sys.exit(0)

   def readInput(argv=argv, inputs=inputs):
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

      def opt_read(inputs, arg):
         """Selects the speak option and saves the text to speak"""
         inputs["input_text"] = arg
         inputs["speak"] = True
         return inputs

      def opt_speed(inputs, arg):
         """Changes the speed of the speaker"""
         inputs["speed"] = int(arg)
         return inputs

      def opt_input_file(inputs, arg):
         """Sets the input file"""
         inputs["input_file"] = arg
         return inputs

      def opt_output_file(inputs, arg):
         """Sets the output file"""
         inputs["output_file"] = arg
         return inputs

      # Try to read the inputs
      try:
         opts, args = getopt.getopt(argv,"hi:o:",["read=","speed=","ifile=","ofile="])
      # If input could net be obtained then exit
      except getopt.GetoptError:
         opt_error()
      # If the inputs could be obtained interpret them
      for opt, arg in opts:
         if opt == options["help"]: 
            opt_help()
         elif opt in options["read"]:        
            inputs = opt_read(inputs, arg) 
         elif opt in options["speed"]:        
            inputs = opt_speed(inputs, arg) 
         elif opt in options["input"]: 
            inputs = opt_input_file(inputs, arg)
         elif opt in options["output"]: 
            inputs = opt_output_file(inputs, arg)

      return inputs

   # First Read the input
   inputs = readInput()

   # Save input text to file
   if inputs["input_file"]:
        f = open(inputs["input_file"],"r")
        inputs.text = f.read()
        saveMp3(text=inputs["input_text"], output_file=inputs["output_file"])
        f.close()

   # Read input text out loud
   if inputs["speak"] and inputs["input_text"]:
        saveMp3(text=inputs["input_text"], output_file="output_file.mp3")
        speak(speed=inputs["speed"], output_file="output_file.mp3")


if __name__ == "__main__":
   main(sys.argv[1:])

