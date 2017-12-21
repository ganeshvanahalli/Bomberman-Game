from __future__ import print_function
import signal
import copy
import sys
import time
from random import randint
from alarmexception import *

#   when the player delays to input the move the board must keep on printing it musn't stop
#   hence for that timeout = 1 second is set


class Get_input:  # implementing using this class
    def __init__(self):
        import tty

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


getch = Get_input()  # getcharacter from the keystrokes.


def alarmHandler(signum, frame):
    raise AlarmException


def input_to(timeout=1):  # timeout is set to 1 .
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
