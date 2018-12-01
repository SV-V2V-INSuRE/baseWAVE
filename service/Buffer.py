import multiprocessing
import time


class Buffer:
    def __init__(self):
        self.queue = multiprocessing.Queue()

    def empty(self):
        return self.queue.empty()

    def read(self):
        while(True):
            if(not self.queue.empty()):
                return self.queue.get()
            time.sleep(.1)


    def write(self, msg):
        print("trying to write: ", msg)
        self.queue.put(msg)