import time
from time import *


def PrintingTest():
    print('hello world')
    exec('print("hello world")')


def RunCodePieces(code: str):
    print(code)
    print('running')
    exec(code)
    # Running the code with method "exec()", that used to run codes in str(String) type.(Look at Basic -> Variables -> Types -> String for information)


def WhileTrue(code: str):
    while True:
        exec(code)
    # Run the code forever.(while True means to run forever. If there is not a break method, it will never stop.)(Break and while True in Basic(Folder) -> Loops -> While)


def ForNTimes(code: str, times: int):
    for i in range(times):
        exec(code)


def TimeState():
    a = time()
    print(a)
    return a


def TimeAccurate():
    a = asctime()
    print(a)
    return a


def sleep(secondsSleeping:int):
    sleep(secondsSleeping)
