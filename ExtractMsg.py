
#####################################################
#              AudioStego Ver 1.0                   #
#              Coded By BlackHammer                 #
#              Hidden Message Extractor             #  
#                 .......Copyright ©2021 Team Black #  
#####################################################

import os
import wave
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='audiofile', dest='audiofile')
args = parser.parse_args()
audio_file = args.audiofile
arged = False
if audio_file:
    arged = True
def clr():
  os.system("clear")
def help():
  print("\033[92mThis Tool Will Help You To Extract The Secrate Msg From Audio File\033[0m")
  print ('''usage: python3 ExtractMsg.py [-h] [-f AUDIOFILE]

optional arguments:
  -h, --help    show this help message and exit
  -f AUDIOFILE  Audio file with secrate msg in it''')
  
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
    

def ex_msg(audio_file):
    if not arged:
      help()
    else:
        print ("Initializing...........!!!")
        wav_audio = wave.open(audio_file, mode='rb')
        frame_bytes = bytearray(list(wav_audio.readframes(wav_audio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
        msg = string.split("###")[0]
        print("Extracted Secrate Msg : \033[1;91m"+msg+"\033[0m")
        wav_audio.close()
clr()
banner()
try:
  ex_msg(audio_file)
except:
  print ("Something went wrong!! try again")
  quit('')

