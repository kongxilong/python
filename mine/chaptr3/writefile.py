#!/usr/bin/python3

'makeTextFile.py--create text file'

import os

ls = os.linesep

#get filename
fname = input('please enter the filename:')
while True:
    if os.path.exists(fname):
        print ( "Error : '%s' already exists" % fname)
    else:
        break

#get file content(text) lines

all = []
print ("\nEnter Lines('.' by itself to quit).\n")

#loop until user terminates input

while True:
    entery = input('>')
    if entery == '.':
        break
    else: 
        all.append(entery)

#wirte lines in file
fobj = open(fname, 'w')
fobj.writelines(['%s%s' %(x, ls) for x in all])
fobj.close()

print ('Done!')


