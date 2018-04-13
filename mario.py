#!/usr/bin/env python
# Based on:
# http://askubuntu.com/questions/508236/how-can-i-run-code-whenever-a-usb-device-is-unplugged-without-requiring-root/
# http://stackoverflow.com/questions/469243/how-can-i-listen-for-usb-device-inserted-events-in-linux-in-python

import functools
import os.path
import pyudev
import subprocess


def main():
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    path = functools.partial(os.path.join, BASE_PATH)
    call = lambda x, *args: subprocess.call([path(x)] + list(args))

    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')
    monitor.start()

    # Call these again whenever a USB device is plugged or unplugged:
    for action, device in monitor:
	# I can add more logic here, to run only certain kinds of devices are plugged.
        vendor_id = device.get('ID_VENDOR_ID')
	# Get vendor_id using lsusb in bash. It is the 4 character alphanumeric string after ID
	if vendor_id in ['0079'] and action == 'add':
		call('mario.sh')
	#call('xinput_disable_mouse_acceleration.sh')
        #call('xset_my_preferences.sh')
	#call('mario.sh')


if __name__ == '__main__':
    main()
