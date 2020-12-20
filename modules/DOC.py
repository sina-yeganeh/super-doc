import os, sys
from colorama import Fore as c
from colorama import init
from frontend import helplist

def MainDoc():
    init()
    while True:
        command = input(c.CYAN + ' \nHome@root/Command/' + c.WHITE + ' $ ')

        # Doc test (send three packet)
        if command == 'doc':
            try:
                target = input(c.BLUE + 'Please enter Url of target' + c.WHITE + ' $ ')
                os.system('ping ' + target)
            except Exception as error:
                print(c.LIGHTBLUE_EX + ' Somthing went wrong | ', error)

        elif command == 'doc -s -inf':
            try:
                target = input(c.BLUE + 'Please enter Url of target' + c.WHITE + ' $ ')
                os.system('ping ' + target + ' -t')
            except Exception as error:
                print(c.LIGHTBLUE_EX + ' Somthing went wrong | ', error)

        elif 'doc -s -inf -sp' in command:
            try:
                target = input(c.BLUE + 'Please enter Url of target' + c.WHITE + ' $ ')
                os.system('ping ' + target + ' -t -l' + str(command[15:]))
            except Exception as error:
                print(c.LIGHTBLUE_EX + ' Somthing went wrong | ', error)

        elif 'doc -s -inf -sp -ip' in command:
            try:
                os.system('ping ' + str(command[22:]) + ' -t -l' + str(command[15:18]))
            except Exception as error:
                print(c.LIGHTBLUE_EX + ' Somthing went wrong | ' + c.RED +  error)

        elif command == 'doc -h':
            helplist.helplist()

        elif command == 'superdoc++':
            helplist.about()

        elif command == 'doc -BT -h':
            print(c.RED + 'Comming Soon...')

        elif command == 'exit':
            sys.exit()

        # for nothing command
        else:
            input(c.BLUE + 'Please enter any Command | ' + c.RED + 'Ctrl + C to exit ')
