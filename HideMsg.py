
#####################################################
#              AudioStego Ver 1.0                   #
#              Coded By BlackHammer                 #
#              Secrate Message Hider                #  
#                 .......Copyright ©2021 Team Black #  
#####################################################

import os
import wave
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', help='Audio file in which you want to hide your message', dest='audiofile')
parser.add_argument('-m', help='our secrate message', dest='secretmsg')
parser.add_argument('-o', help='Your output file name', dest='outputfile')
args = parser.parse_args()

audio_file = args.audiofile
string = args.secretmsg
output = args.outputfile
arged = False
if audio_file and string and output:
    arged = True

def clr():
  os.system("clear")

def help():
  print("\033[92mThe Tool That Helps You To Hide Your Secrate Msg In Audio File\033[0m")
  print ('''usage: python3 HideMsg.py [-h] [-f AUDIO_FILE] [-m SECRET_MESSAGE] [-o OUTPUT_FILE]

optional arguments:
  -h, --help    show this help message of the script
  -f AUDIOFILE  Audio file in which you want to hide your message
  -m SECRETMSG  Your secrate message
  -o OUTPUTFILE Your output file name ''')
  
def banner():
    clr()
    os.system('figlet -f slant AudioStego | lolcat')
    os.system('echo "\e[1;34m Created By \e[1;32m"')
    os.system('toilet -f mono12 -F border "TEAM      BLACK" | lolcat')
    os.system('echo "For Any Queries Mail Us!!!" | lolcat')
    os.system('echo "        Mail: thedarktech.yt@gmail.com" | lolcat')
    os.system('echo " YouTube Page: https://www.youtube.com/channel/UC6_l3aewNJpPYSkg0TpxSCA " | lolcat')
    os.system('echo " "')
    print("\n")
    
def add_msg(audio_file, string, output):
    if not arged:
      help()
    else:
      print ("Initializing.........")
      wav_audio = wave.open(audio_file, mode='rb')
      frame_bytes = bytearray(list(wav_audio.readframes(wav_audio.getnframes())))
      string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
      bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
      for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
      frame_modified = bytes(frame_bytes)
      with wave.open(output, 'wb') as fd:
        fd.setparams(wav_audio.getparams())
        fd.writeframes(frame_modified)
      wav_audio.close()
      print ("Process Completed.......")
clr()
banner()
try:
  add_msg(audio_file, string, output)
except:
  print ("Something went wrong........!!")
  print("Please try again........")
  quit('')
