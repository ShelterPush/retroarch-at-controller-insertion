#!/bin/bash

# Check if the script actually launches
echo "Mario" >> /tmp/mariocheck.tmp
# Require that this script only run if retroarch isn't already running (probably redundant, but it works)
if ! pgrep -x "retroarch" > /dev/null
then
	retroarch -f -L /usr/lib/libretro/mupen64plus_libretro.so ~/Mario\ Kart\ 64.n64
else
	echo "Retroarch is already running" >> /tmp/retroarchcheck.tmp
fi
