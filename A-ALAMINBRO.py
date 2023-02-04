
import os, platform

 

try:

 

        import requests

 

except:

 

        os.system('pip2 install requests')

 

 

 

bit = platform.architecture()[0]

 

if bit == "64bit":

        os.system('xdg-open https://youtube.com/@teach-alamin')

 

        from ALAMIN import alaminbro

 

        ALAMIN()

 

 

 

elif bit == "32bit":

 

        os.system('xdg-open https://youtube.com/@teach-alamin')

 

        os.system('python ALAMINBRO.py')
