# retroarch-at-controller-insertion
A bash script and a python script that work together to launch a game using RetroArch once a controller (or other specified input device) is connected using pyudev on Linux.\
You have to have pip in order to install pyudev.\
If you don't have pip (my image didn't), run 
```bash
sudo apt-get install python-pip
```
Once it is installed, run
```bash
sudo -H pip install pyudev
```
to install pyudev.\
The -H flag makes pip happy; honestly, I'm not sure why. However, when I tried to install pyudev without sudo it couldn't do it, and whenever I tried to do it with sudo it recommended to use the -H flag, so I did. (man sudo says that -H sets the HOME environment variable to the home directory specified by the target user's password database entry)\
After you have pyudev installed, you should edit the directory in mario.sh to reflect the game and system you would like to use. Refer to https://docs.libretro.com/guides/cli-intro/ for more information.\
Run the script like normal with
```bash
python mario.py
```
It should launch whatever your specified game is.

Credit to [Denilson](https://askubuntu.com/users/8668/denilson-s%c3%a1-maia) for [this answer](https://askubuntu.com/a/516336) at askubuntu for the majority of the code. \
I was advised to upload this since all of this info was surprisingly difficult to find.
