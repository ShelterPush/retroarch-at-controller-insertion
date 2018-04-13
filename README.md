# retroarch-at-controller-insertion
A bash script and a python script that work together to launch a game using RetroArch once a controller (or other specified input device) is connected using pyudev on Linux.
You have to have pip in order to install pyudev.
If you don't have pip, run 

sudo apt-get install python-pip

Once it is installed, run

sudo -H pip install pyudev

to install pyudev.
After you have pyudev installed, you should edit the directory in mario.sh to reflect the game and system you would like to use. Refer to https://docs.libretro.com/guides/cli-intro/ for more information.

Credit to this answer at askubuntu for the majority of the code: https://askubuntu.com/a/516336
I was advised to upload this since all of this info was surprisingly difficult to find.
