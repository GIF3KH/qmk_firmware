# Image to Hex Converter
# Copyright (c) 2018 MakotoKurauchi
# MIT License

from PIL import Image
from numpy import *
import sys

argvs = sys.argv
argc = len(argvs)

if (argc != 2):
	print ('Usage: $ python %s filename' % argvs[0])
	quit()

im = array(Image.open(argvs[1]))

fontw = 8
fonth = 8
wmax = 128//fontw
hmax = 64//fonth

for hc in range(hmax):
	for wc in range(wmax):
		line = ""
		for fonthc in range(fonth):
			val=0
			for fontwc in reversed(range(fontw)):
				b = 1 if im[fonth*hc+fonthc][fontw*wc+fontwc][0]>128 else 0
				val = (val<<1)|b
			line += '0x%02X' % val + ', '
		print (line)
