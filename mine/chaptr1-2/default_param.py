#!/usr/bin/python3


def foo(debug=True):
    if debug:
        print('cur in debug mode')
    else:
        print('cur in realse mode') 
    print('done')



foo(False)


