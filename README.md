# Raspberry-Pi-Updater
Finished Raspberry Pi updater (Python)
After a few days of working on my initial repository (the repo was private) for and updater script, I have completed it. Please be aware that this was my first attempt at learing python through a hands on approach. The script does the following:

1) Checks EUID to make sure that the Root User is running it
2) Asks if the script is being run on a raspberry pi
  2A) If answered with "yes" it says, "This will update the raspberry pi"
  2B) If answered with "no" it says, "This most likely will not work on this device, I apologise"
3) If answered with yes in the previous question, it will begin to update and upgrade the raspberry pi
4) Finally, it displays the current linux identification and version number.

*There is a known issue with the updater going on loop, I am working to fix that and implement an exit method.*
