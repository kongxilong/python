#!/usr/bin/python3


'readTextFile.py--read and display text file'

#get file name

fname = input('please input the file to read:')


try:
    fobj = open(fname,'r')
except:
    print("*** file open error" ,e)
else:
    #display the contents of the file to the screen.

    for eachline in fobj:
        print(eachline,)
    fobj.close()



