#!/opt/pwn.college/python

import subprocess
import struct
import os

sprites = { }
operations = [ ]
for c in open("/flag").read().strip():
	if c not in sprites:
		sprites[c] = len(operations)
		sprite = subprocess.check_output(["/usr/bin/figlet", c]).split(b"\n")[:-1]
		operations += [ struct.pack("<HBBB", 3, sprites[c], len(sprite[0]), len(sprite)) + b"".join(sprite) ]
	operations += [ struct.pack("<HBBBBBB", 4, sprites[c], 0xff, 0xff, 0xff, 0, 0) ]

img = b"cIMG" + struct.pack("<HBBI", 3, 16, 16, len(operations)) + b"".join(operations)
with open("/challenge/the_flag.cimg", "wb") as o:
	o.write(img)
