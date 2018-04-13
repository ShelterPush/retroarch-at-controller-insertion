#!/bin/bash

echo "Mario" >> /tmp/mariocheck.tmp
if ! pgrep -x "retroarch" > /dev/null
then
	retroarch -f -L /usr/lib/libretro/mupen64plus_libretro.so ~/Mario\ Kart\ 64.n64
else
	echo "Retroarch is already running" >> /tmp/retroarchcheck.tmp
fi
