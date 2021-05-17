#timer class will house all the functionality that has to do with implementing timers
import time

# static variable that will house all the current timers
# will be used when we want to implement the deleting timer functionality
timers = dict()

# t = time in seconds
def __init__(self, t):
	self.t = t

