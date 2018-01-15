#!/usr/bin/python3


class Myfoo(object):
    version = 0.1

    def __init__(self,nm='John Doe'):
        self.name = nm
        print('created a class instance for',nm)
        print('this is a ','test')

    def showname(self):
        print('your name is ', self.name)

    def showverison(self):
        print( self.version)


foo = Myfoo()



