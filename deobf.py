# scripted by samay
# Deobfuscated by Fufly
# esp8266 wifi jammer setup through script
# Encrypted by samay 
# Author : Samay 
# Normally all setup through script 

# --- modules 

import os 
import sys
try:
    import colorama
    import requests
    import wget
except ImportError:
    os.system(\'pip install colorama\' if os.name==\'nt\' else \'pip3 install colorama\')
    os.system(\'pip install requests\' if os.name==\'nt\' else \'pip3 install requests\')
    os.system(\'pip install wget\' if os.name==\'nt\' else \'pip3 install wget\')
import wget
import shutil
from time import sleep
from zipfile import ZipFile
from colorama import Fore
from getpass import getpass


# --- colors 
r = "\\033[1;31m"
g = "\\033[1;32m"
y = "\\033[1;33m"
b = "\\033[1;34m"
d = "\\033[2;37m"
R = "\\033[1;41m"
Y = "\\033[1;43m"
B = "\\033[1;44m"
w = "\\033[1;37m"
g = "\\033[0;90m"
y = r

# ---- banner and functions 

logo = \'\'\'
    \\033[1;31m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97        \\033[1;35m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97
    \\033[1;32m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91        \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91
    \\033[0;90m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \\033[1;32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\\033[1;33m    \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\033[1;33m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91
    \\033[1;33m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \\033[1;34m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d    \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91
    \\033[1;35m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91           \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91
    \\033[1;31m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d           \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d    \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d
\'\'\'

def banner():
    print(logo)

def clear():
    os.system(\'cls\' if os.name==\'nt\' else \'clear\')

def _under_():
    print(\'\
\')

def aboutus():
    string = """ 
    \\033[1;37mDeveloper  \\033[1;34m: \\033[1;31mSamay825
    \\033[1;37mGithub     \\033[1;34m: \\033[1;31mSamay825
    \\033[1;37mInstagram  \\033[1;34m: \\033[1;31m@sincryptzork
    """
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.01)
    _under_()

def folder(khushi):
    if not os.path.exists(khushi):
        os.makedirs(khushi)


def printcontent(samay):
    print(r+"\xe2\x94\x94\xe2\x94\x80> "+w+"\\033[1;37m"+samay)

def optionsfront():
    clear()
    banner()
    aboutus()
    printcontent(\'[ 1 ] Wifi Jammer Setup\')
    printcontent(\'[ 2 ] Instructions \')
    printcontent(\'[ 3 ] About me \')
    printcontent(\'[ 4 ] Update\')
    printcontent(\'[ 5 ] Exit \')
    _under_()

optionsfront()

def frontclearsecond():
    clear()
    banner()
    _under_()

# --- Object oriented programming 

class Samay:
    project = \'Nodemcu esp8266\'
    def __init__(self,data):
        self.data = data
    def functions(self):
        if self.data==1:
            folder(\'Wifi-Jammer-Setup\')
            frontclearsecond()
            samayfunctions = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mDo you have nodemcu esp8266 or other version ? [y/n] : "+r)
            if samayfunctions==\'Y\' or samayfunctions==\'y\':
                frontclearsecond()
                printcontent(\'[ 1 ] Chip CP2102\')
                printcontent(\'[ 2 ] Chip CP340\')
                _under_()
                samayfuc1 = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Desire options : "+r))
                if samayfuc1==1:
                    _under_()
                    printcontent(\'Downloading CP2102 Windows Driver ..\'+g)
                    try:
                        wget.download(\'https://www.silabs.com/documents/public/software/CP210x_Windows_Drivers.zip\')
                        _under_()
                        shutil.move(\'CP210x_Windows_Drivers.zip\',\'Wifi-Jammer-Setup/\')
                        printcontent(\'Downloading Nodemcu flasher ..\')
                        wget.download(\'https://github.com/nodemcu/nodemcu-flasher/archive/refs/heads/master.zip\')
                        _under_()
                        shutil.move(\'nodemcu-flasher-master.zip\',\'Wifi-Jammer-Setup/\')
                        printcontent(\'Downloading nodemcu file bin ..\')
                        wget.download(\'https://github.com/SpacehuhnTech/esp8266_deauther/releases/download/2.6.1/esp8266_deauther_2.6.1_NODEMCU.bin\')
                        _under_()
                        shutil.move(\'esp8266_deauther_2.6.1_NODEMCU.bin\',\'Wifi-Jammer-Setup/\')
                        frontclearsecond()
                        printcontent(\'All requirements downloaded \')
                        printcontent(\'Please wait ..\')
                        sleep(2.3)
                        frontclearsecond()
                        printcontent(\'Extract the two files present in Wifi-Jammer-Folder\')
                        _under_()
                        oks = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mExtracted zip ? [ y/n ] : "+r).strip()
                        if oks==\'y\' or oks==\'Y\':
                            samaysir2 = True
                        else:
                            printcontent(\'Extract now ..\')
                            samaysir2 = False
                     
                    except:
                        pass


                    if samaysir2:
                        os.startfile(\'Wifi-Jammer-Setup\\\\CP210x_Windows_Drivers\\\\CP210xVCPInstaller_x64.exe\')
                        sleep(2.0)
                        os.startfile(\'Wifi-Jammer-Setup\\\\nodemcu-flasher-master\\\\nodemcu-flasher-master\\\\Win64\\\\Release\\\\ESP8266Flasher.exe\')
                        sleep(1.0)
                        frontclearsecond()
                        printcontent(\'plug in with datacable nodemcu now and select advanced option in flasher ..\')
                        _under_()
                        printcontent(\'baudrate size : 9600\')
                        printcontent(\'flash size : 1 mb\')
                        printcontent(\'flash speed : 80 mhz \')
                        printcontent(\'SPI MODE : DIO\')
                        _under_()
                        printcontent(\'Now select the config file from wifi-jammer-setup folder named nodemcu.bin shown in the youtube visit ..\')
                        _under_()
                        printcontent(\'now start the flash ......\')
                        printcontent(\'after flash connect to the new wifi named pwned  password is : deauther\')
                        printcontent(\'now open browser go to this ip : 192.168.4.1\')
                        printcontent(\'enjoy .....\')
                        print(\'\n\')
                    elif samaysir2==False:
                        ss = input(\'Extracted ?  [y/n] : \')
                        if ss==\'y\':
                            os.startfile(\'Wifi-Jammer-Setup\\\\CP210x_Windows_Drivers\\\\CP210xVCPInstaller_x64.exe\')
                            sleep(2.0)
                            os.startfile(\'Wifi-Jammer-Setup\\\\nodemcu-flasher-master\\\\nodemcu-flasher-master\\\\Win64\\\\Release\\\\ESP8266Flasher.exe\')
                            frontclearsecond()
                            printcontent(\'plug in with datacable nodemcu now and select advanced option in flasher ..\')
                            _under_()
                            printcontent(\'baudrate size : 9600\')
                            printcontent(\'flash size : 1 mb\')
                            printcontent(\'flash speed : 80 mhz \')
                            printcontent(\'SPI MODE : DIO\')
                            _under_()
                            printcontent(\'Now select the config file from wifi-jammer-setup folder named nodemcu.bin shown in the youtube visit ..\')
                            _under_()
                            printcontent(\'now start the flash ......\')
                            printcontent(\'after flash connect to the new wifi named pwned  password is : deauther\')
                            printcontent(\'now open browser go to this ip : 192.168.4.1\')
                            printcontent(\'enjoy .....\')
                            print(\'\n\')








                elif samayfuc1==2:
                    _under_()
                    printcontent(\'Downloading CP304 Windows Driver ..\'+g)
                    try:
                        wget.download(\'https://sparks.gogo.co.nz/assets/_site_/downloads/CH34x_Install_Windows_v3_4.zip\')
                        _under_()
                        shutil.move(\'CH34x_Install_Windows_v3_4.zip\',\'Wifi-Jammer-Setup/\')
                        printcontent(\'Downloading Nodemcu flasher ..\')
                        wget.download(\'https://github.com/nodemcu/nodemcu-flasher/archive/refs/heads/master.zip\')
                        _under_()
                        shutil.move(\'nodemcu-flasher-master.zip\',\'Wifi-Jammer-Setup/\')
                        printcontent(\'Downloading nodemcu file bin ..\')
                        wget.download(\'https://github.com/SpacehuhnTech/esp8266_deauther/releases/download/2.6.1/esp8266_deauther_2.6.1_NODEMCU.bin\')
                        _under_()
                        shutil.move(\'esp8266_deauther_2.6.1_NODEMCU.bin\',\'Wifi-Jammer-Setup/\')
                        frontclearsecond()
                        printcontent(\'All requirements downloaded \')
                        printcontent(\'Please wait ..\')
                        sleep(2.3)
                        frontclearsecond()
                        printcontent(\'Extract the two files present in Wifi-Jammer-Folder\')
                        _under_()
                        oks = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mExtracted zips ? [ y/n ] : "+r).strip()
                        if oks==\'y\' or oks==\'Y\':
                            samaysir = True
                        else:
                            printcontent(\'Extract now ..\')
                            samaysir = False
                     
                    except:
                        pass

                    if samaysir==True:
                        ss = input(\'Extracted ?  [y/n] : \')
                        if ss==\'y\':
                            os.startfile(\'Wifi-Jammer-Setup\\\\CH34x_Install_Windows_v3_4\\\\CH34x_Install_Windows_v3_4.EXE\')
                            sleep(2.0)
                            os.startfile(\'Wifi-Jammer-Setup\\\\nodemcu-flasher-master\\\\nodemcu-flasher-master\\\\Win64\\\\Release\\\\ESP8266Flasher.exe\')
                            sleep(1.0)
                            frontclearsecond()
                            printcontent(\'plug in with datacable nodemcu now and select advanced option in flasher ..\')
                            _under_()
                            printcontent(\'baudrate size : 9600\')
                            printcontent(\'flash size : 1 mb\')
                            printcontent(\'flash speed : 80 mhz \')
                            printcontent(\'SPI MODE : DIO\')
                            _under_()
                            printcontent(\'Now select the config file from wifi-jammer-setup folder named nodemcu.bin shown in the youtube visit ..\')
                            _under_()
                            printcontent(\'now start the flash ......\')
                            printcontent(\'after flash connect to the new wifi named pwned  password is : deauther\')
                            printcontent(\'now open browser go to this ip : 192.168.4.1\')
                            printcontent(\'enjoy .....\')
            elif samayfunctions==\'N\' or samayfunctions==\'n\':
                _under_()
                printcontent("You can\'t perform wifi jammer without node-MCU please buy the Nodemcu ")
                printcontent(\'Link to buy : \'+Fore.GREEN+\'https://amzn.to/3LjeBmm\')
                sys.exit(\'\n\'+r+"\xe2\x94\x94\xe2\x94\x80"+w+"Comeback with nodemcu and re run script !\n")
                _under_()
        #

        elif self.data==2:
            samay = Fore.BLUE+\'\'\'\
This software allows you to easily perform a variety of actions to test 802.11 wireless networks by using an inexpensive ESP8266 WiFi SoC (System On A Chip).

The main feature, the deauthentication attack, is used to disconnect devices from their WiFi network.
No one seems to care about this huge vulnerability in the official 802.11 WiFi standard, so I took action and enabled everyone who has less than 10 USD to spare to recreate this project.
I hope it raises more attention on the issue. In 2009 the WiFi Alliance actually fixed the problem (see 802.11w), but only a few companies implemented it into their devices and software.
To effectively prevent a deauthentication attack, both client and access point must support the 802.11w standard with protected management frames (PMF).
While most client devices seem to support it when the access point forces it, basically no WiFi access point has it enabled.

Feel free to test your hardware out, annoy these companies with the problem, share this project and push for a fix! This project is also a great way to learn more about WiFi, micro controllers, Arduino, hacking and electronics/programming in general.
But please use this tool responsibly and do not use it against others without their permission!\
\'\'\'
            print(samay)

        elif self.data==3:
            samay23 = Fore.GREEN+\'\'\'hi, i\'m Ethical Hacker Zork, a passionate self-taught Powerful Ethical Hacker and C,C++,JS,Shell and Python developer and a freelance software engineer from india. my passion for software lies with dreaming up ideas and making them come true with elegant interfaces. i take great care in the experience, architecture, and code quality of the things I build.

i am also an open-source enthusiast and maintainer. i learned a lot from the open-source community and i love how collaboration and knowledge sharing happened through open-source.\'\'\'
            print(samay23)


        elif self.data==4:
            os.system(\'python update.py\' if os.name==\'nt\' else \'python3 update.py\')

        elif self.data==5:
            _under_()
            printcontent(\'Exiting...\')
            _under_()
            sys.exit()

        

try:
    selfdata = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Desire option : "+r))
except:
    _under_()
    printcontent(\'Please put the number to select options ! \')
    sys.exit(\'\
Exiting...\')

if __name__ == \'__main__\':
    Vrushabh = Samay(selfdata)
    Vrushabh.functions()
