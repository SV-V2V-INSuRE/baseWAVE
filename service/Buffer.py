import multiprocessing
import time


class Buffer:
    def __init__(self):
        self.Queue = multiprocessing.Queue()

    def read(self):
        while(True):
            if(not self.Queue.empty()):
                return self.Queue.get()
            time.sleep(.1)


    def write(self, msg):
        self.Queue.put(msg)