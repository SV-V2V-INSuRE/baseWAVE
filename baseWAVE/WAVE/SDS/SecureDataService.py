from service import Service,SAP,Message

class SecureDataService(Service.Service):
    def __init__(self, logger=None):
        #inherits Service
        Service.Service.__init__(self, name = "SDS", logger=logger)

    #assume SAPs are already bound
    def start(self):
        #send test messages
        self.send("SSME-Sec-SAP", self.getMessage("test.request",("SDS Originating",)))

        self.listen(self.handle)


    def handle(self, msg, resp_buffer):
        self.LogInfo("Received message of type " + msg.name)
        if(msg.name == "test.request"):
            self.respond(resp_buffer, "test.confirm",("confirm",))

        elif(msg.name == "test.confirm"):
            self.LogInfo("CONNECTION TO {} CONFIRMED".format(msg.source))
            
        else:
            self.LogInfo("Received unknown message type: " + msg.name)