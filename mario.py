#!/usr/bin/env python
# Based on:
# http://askubuntu.com/questions/508236/how-can-i-run-code-whenever-a-usb-device-is-unplugged-without-requiring-root/
# http://stackoverflow.com/questions/469243/how-can-i-listen-for-usb-device-inserted-events-in-linux-in-python
# https://askubuntu.com/a/516336

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
	# This next part is to run only when a device is inserted.
	# Previously, retroarch would launch both when I inserted my controller and when I removed it.
	# It also filters by device, so that I could insert any other device and not have retroarch launch.
        vendor_id = device.get('ID_VENDOR_ID')
	# Find the vendor_id using lsusb in bash. It is the 4 character alphanumeric string after ID
	if vendor_id in ['0079'] and action == 'add': # 0079 is the vendor ID of my controller
		call('mario.sh')
	# If you want something to run every time you insert or remove any input device,
	# you should be able to just comment out my if statement and add the desired command here.
	# If that doesn't work, replace 
	#for action, device in monitor:
	# with 
	#for device in iter(monitor.poll, None):
	# That's what I had before I learned how to run this only when a specific device is plugged in.
	# Commented out the unnecessary commands from the original and my original command.
	#call('xinput_disable_mouse_acceleration.sh')
        #call('xset_my_preferences.sh')
	#call('mario.sh')


if __name__ == '__main__':
    main()
