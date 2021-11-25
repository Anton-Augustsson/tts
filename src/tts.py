#!/usr/bin/python3
from gtts import gTTS
from playsound import playsound
import sys, getopt
import os 

def saveMp3(text,outputfile):
    tts = gTTS(text)
    tts.save(outputfile)
    
def readText(outputfile, speed=2):
    #playsound(outputfile)
    os.system(f'mpg123 --doublespeed "{speed}" ' + outputfile)
    sys.exit(0)


# Text to speech
## Example 1 - read higlighted text: tts.py
## Example 2 - read txt file and save to mp3: tts.py -i someInputFile.txt -o someOutputFile.mp3  
def main(argv):
   inputfile = ''
   outputfile = ''
   text = ''
   read = False
   standardOutputfile = 'output.mp3'

   try:
      opts, args = getopt.getopt(argv,"hi:o:",["read=","ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("--read"):
         text = arg
         read = True
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   if inputfile:
        f = open(inputfile,"r")
        text = f.read()
        saveMp3(text=text, outputfile=outputfile)
        f.close()
        

   if read and text:
        saveMp3(text=text, outputfile=standardOutputfile)
        readText(outputfile=standardOutputfile)


if __name__ == "__main__":
   main(sys.argv[1:])

