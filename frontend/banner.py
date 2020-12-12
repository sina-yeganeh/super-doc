import os
from colorama import Fore as c
reset='\033[0m'
bold='\033[01m'

def banner():
    os.system('cls' or 'clear')
    print(c.LIGHTBLUE_EX + '''
   ___ _   _ ___ ___ ___
  / __| | | | _ \ __| _ \ V.1.1
  \__ \ |_| |  _/ _||   /
  |___/\___/|_|_|___|_|_\_
 |   \ / _ \ / __|| |_ _| |_
 | |) | (_) | (_|_   _|_   _|
 |___/ \___/ \___||_|   |_|''')
    print(c.GREEN + '       BY UpstartCoder')
    print(c.WHITE + '[Write doc -h To get Information]')
