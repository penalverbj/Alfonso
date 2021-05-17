#timer class will house all the functionality that has to do with implementing timers
import time

#static variable that will house all the current timers
#will be used when we want to implement the deleting timer functionality
timers = dict()

#t = time in seconds that serves as value
#name = name string that serves as key
def __init__(self, name, t):
  self.name = name
  self.t = t
  timers[name] = t # adds new timer to dictionary with key:value pair name:time

