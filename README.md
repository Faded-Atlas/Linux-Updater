# Linux-Updater
# Keep in mind that this is only for machines running a distribution of Linux!
Linux Updater
Language: Python
Compatability: Linux machines (Includes ARM devices loaded with linux and Re4son kernels)

After a few days of working on my initial repository (the repo was private) for and updater script, I have completed it. Please be aware that this was my first attempt at learing python through a hands on approach. The script does the following:

1) Checks EUID to make sure that the Root User is running it.
2) Asks if the script is being run on a Linux machine.
  2A) If answered with "yes" it says, "This will update your machine".
  2B) If answered with "no" it says, "This most likely will not work on this device, I apologise".
3) If answered with yes in the previous question, it will begin to update and upgrade the computer.
4) When done updating, it displays the current linux identification and version number.
5) Finally, it prints "Update/Upgrade finished!" and exits.

*Fork/purpose change if I missed something
