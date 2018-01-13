#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
#import re
import time

'readTextFile.py--read and display text file'
# 格式化成2016-03-20 11:45:39形式
#print time.strftime("%Y%m%d%H%M%S_log", time.localtime()) 
#get source file name


while True:
    fsrcname = raw_input('Please input the file to read:')
    if not os.path.exists(fsrcname):
        print "Error : '%s' isn't exists." % fsrcname
    else:
        print "success : '%s' is exists." % fsrcname
        break


while True:
    fdestpath = raw_input('Please input the dest file path to output:')
    if not os.path.isdir(fdestpath):
        print "Error : '%s' isn't exists." % fdestpath
    else:
        print "success : '%s' is ok." % fdestpath
        break

filterstr = []   #word to match



while True:
    restr = raw_input('Please input the word to match for the lines in log,input :q to quit:')
    if restr == ':q':
        print "\r\n matching ...,please wait"
        break
    elif restr == '':
        print "Please input valid word to match"
    else:
        filterstr.append(restr)

all = []
try:
    fobj = open(fsrcname,'r')
    lines = fobj.readlines()
except:
    print("*** file open error" )
else:
#display the contents of the file to the screen.
    for eachline in lines:
        for eachword in filterstr:
            m = eachline.find(eachword)
            # if m is not None:
            if m >= 0:
                # print m.group()
                all.append(eachline)
                break
    fobj.close()

if all is not None:
    destfilename = time.strftime("%Y%m%d%H%M%S", time.localtime())
    destfilename = destfilename + '.log'

    if fdestpath.endswith('\\') or fdestpath.endswith('/'):
        fdestpath = fdestpath + destfilename
    else:
        fdestpath = fdestpath + '\\'+ destfilename

    print "filter file complete, now the output the result to the '%s' " % fdestpath

    try:
        fobj = open(fdestpath,'w')
    except:
        print("*** file open error")
    else:
        #display the contents of the file to the screen.
        for eachline in all:
            fobj.writelines(eachline)
        fobj.close()
        print "file output success, filepath is '%s' " % fdestpath
else:
    print "filter file fail, no match "

