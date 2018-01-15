#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
'readTextFile.py--read and display text file'
#用于统计每个窗口中消息过滤器的类型及每个类型的个数   消息过滤器以":"为分隔符


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

dict = {}   

try:
    fobj = open(fsrcname,'r')
    lines = fobj.readlines()
except:
    print("*** file open error" )
else:
#display the contents of the file to the screen.
    for eachline in lines:  
        index = eachline.index(':')
        # if m is not None:
        if index >= 0:
            key = eachline[0:index]
            if dict.has_key(key):
                value = dict.get(key)
                dict[key] = value + 1
            else:
                dict[key] = 1
            # print m.group()
    fobj.close()

if dict is not None:
    destfilename = time.strftime("%Y%m%d%H%M%S", time.localtime())
    destfilename = destfilename + '.txt'

    if fdestpath.endswith('\\') or fdestpath.endswith('/'):
        fdestpath = fdestpath + destfilename
    else:
        fdestpath = fdestpath + '\\'+ destfilename

    print "filter log complete, now the output the result to the '%s' " % fdestpath

    try:
        fobj = open(fdestpath,'w')
    except:
        print("*** file open error")
    else:
        #display the contents of the file to the screen.
        for key in dict.keys():
            fobj.writelines("key='%s' value=%d;\r\n" % (key,dict[key]))
        fobj.close()
        print "file output success, filepath is '%s' " % fdestpath
else:
    print "filter file fail, no match "

