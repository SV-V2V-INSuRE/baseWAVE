from . import Buffer, SAP, Message


class Service:
    def __init__(self,name="UNNAMED",logger=None):
        self.in_buffers = []
        self.buffers_in_to_out = {}
        self.buffers_in_to_name = {}
        self.name_to_out_buf = {}
        self.running=False
        self.logger = logger
        self.name=name


    def bindSAP(self, sap, reverse_flow=False):
        in_buf = sap.InBuffer
        out_buf = sap.OutBuffer 
        if reverse_flow:
            temp = in_buf
            in_buf = out_buf
            out_buf = temp

        self.buffers_in_to_out[in_buf] = out_buf
        self.buffers_in_to_name[in_buf] = sap.name
        self.name_to_out_buf[sap.name] = out_buf


    def stop_listening(self):
        self.running=False


    def listen(self, handler_func):
        self.LogInfo("Listening...")
        self.running=True
        while self.running:
            for buf in self.buffers_in_to_out.keys():
                if not buf.empty():
                    sap_name = self.buffers_in_to_name[buf]
                    msg = buf.read()
                    self.LogInfo("received message via SAP {}".format(sap_name))
                    handler_func(msg, self.buffers_in_to_out[buf])  #calls handler function with message and response channel


    def send(self, sap_name, msg):
        self.LogInfo("sending {} via SAP {}".format(msg,sap_name))
        #get SAP for this name
        out = self.name_to_out_buf[sap_name]
        out.write(msg)


    def LogInfo(self, msg):
        msg = self.name + ":" + msg
        if self.logger:
            self.logger.LogInfo(msg)

    def respond(self,resp_buffer,name, content):
        resp_buffer.write(Message.Message(self.name,"test.confirm","confirm"))

    def getMessage(self,name,content):
        return Message.Message(self.name, name, content)

#test functionality
def _test1(s):
    def resp(x, out):
        print(x)
        out.write("bye")
        s.stop_listening()

    s.listen(resp)


def _test2(s):
    def resp(x, out):
        print(x)
        s.stop_listening()

    s.send("test","hi")
    s.listen(resp)


if __name__ == '__main__':
    import multiprocessing

    sap = SAP.SAP("test")
    ser1 = Service()
    ser2 = Service()

    sap.bind(ser1,ser2)


    # spawn tests
    p1 = multiprocessing.Process(target = _test1, args=(ser1,))
    p1.start()
    p2 = multiprocessing.Process(target = _test2, args=(ser2,))
    p2.start()

    p1.join()
    p2.join()
    