import os
import time
class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'



def main():
    print(bcolors.BLUE + bcolors.BOLD)
    print("""
  
████████╗░█████╗░░██████╗██╗░░██╗░█████╗░███╗░░░███╗░█████╗░████████╗░█████╗░██████╗░
╚══██╔══╝██╔══██╗██╔════╝██║░██╔╝██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
░░░██║░░░███████║╚█████╗░█████═╝░██║░░██║██╔████╔██║███████║░░░██║░░░██║░░██║██████╔╝
░░░██║░░░██╔══██║░╚═══██╗██╔═██╗░██║░░██║██║╚██╔╝██║██╔══██║░░░██║░░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║██████╔╝██║░╚██╗╚█████╔╝██║░╚═╝░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝ A task automater
    


    Choose the following tasks: 

    1.Make boilerplate: html,css,javascript
    2.Start systemwide tor proxy: torproxy using ghoster
    3.Browse Privatly with ghost-browser and tor proxy:ghoster + ghost browser
    """)
    task = input("Enter the task: ")
    if task == "1":
        print("connecting..")
        print("authenticating...")
        print("connecting to git..")
        print("initiating https protocol")
        print("making a secure ssh tunnel...")
        print("ready!")
        os.system("git clone https://github.com/thefoxis/html-boilerplate.git")
    elif task == "2":
        print("connecting..")
        print("authenticating...")
        print("switching to threads...")
        print("authenticating keys..")
        print("securing network connection...")
        print("initiating...")
        time.sleep(3)
        print("requesting tor node...")
        print("ready!")
        os.system("sudo python3 torghost2.py")

    elif task == "3":
        print("connecting..")
        print("authenticating...")
        print("switching to threads...")
        print("authenticating keys..")
        print("securing network connection...")
        print("initiating...")
        time.sleep(3)
        print("requesting tor node...")
        print("ready!")
        os.system("sudo ./start.sh")
    
    print(bcolors.ENDC)	
    

main()