#timer class will house all the functionality that has to do with implementing timers
import time


class Timer:
    #static variable that will house all the current timers
    #will be used when we want to implement the deleting timer functionality
    timers = {}

    #t = time in seconds that serves as value
    #name = name string that serves as key
    def __init__(self, name, t):
        self.name = name
        self.t = t
        Timer.timers.update({name: t})
