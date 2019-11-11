import os
import time
from time import sleep
import sys

if os.geteuid() != 0:
    exit("Error, try running as root")

a = input("Is running on a Raspberry Pi?")
if "yes" in a:
    while True:
        print("This will update the raspberry pi")
        sleep(5)
        os.system("apt-get update && apt-get full-upgrade -y")
        sleep(2)
        os.system("uname -a")
        exit()

else:
    exit("This most likely will not work on this device, I apologise")
