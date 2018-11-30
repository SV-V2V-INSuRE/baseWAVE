import threading, queue

class MethodCall:
    def __init__(self, caller, method, params):
        self.caller = caller
        self.method = method
        self.params = params


class BasicService:
    def __init(self,logger):
        self.logger = logger

        self.EventTrigger = threading.Event()
        self.CallQueue = queue.Queue()


    def call(self, caller, method, params):
        call = MethodCall(caller, method, params)
        self.CallQueue.put(call)

        #trigger the event
        self.EventTrigger.set()


    # callback_dict is a dictionary of names to anon functions in the form of callback(caller,params)
    def listen(self, callback_dict):
        while True:
            self.EventTrigger.wait()
            while not self.CallQueue.empty():
                call = self.CallQueue.get()
                try:
                    callback_dict[call.method](call.caller,call.method)
                except:
                    self.logger.LogException()