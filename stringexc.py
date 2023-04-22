# import classexc as cl_exc
from classexc import *

for func in (raiser0, raiser1, raiser2, raiser3):
    try:
        func()
    except General:
        import sys

        print('caught: ', sys.exc_info()[0])
