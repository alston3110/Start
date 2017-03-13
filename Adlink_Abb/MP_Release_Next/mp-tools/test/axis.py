#!/usr/bin/python
import struct
from math import sqrt

x = 0
y = 0
z = 0
secondsensorfile = "/dev/input/event1"
#int, int, short, short, int
fmt = 'iihhi'
#open file in binary mode
in_file = open(secondsensorfile,"rb")
event = in_file.read(16)
while event:
	(time1,time2, type, code, value) = \
		struct.unpack(fmt,event)
	time = time2 / 1000.0

	if type == 2 or type == 3:
		if code == 0:
			x = value
		if code == 1:
			y = value
		if code == 2:
			z = value
	if type == 0 and code == 0:
		sum = int(sqrt(x*x + y*y + z*z))
		print time, x, y, z, sum
	event = in_file.read(16)
in_file.close()

