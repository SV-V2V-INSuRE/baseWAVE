from service import Service,SAP,Message

class P2PCertDistributionEntity(Service.Service):
    def __init__(self, logger=None):
        Service.Service.__init__(self, name = "P2PCD", logger=logger)

    #assume SAPs are already bound
    def start(self):
        #send test messages
        self.send("SSME-SAP", self.getMessage("test.request",("P2PCDE Originating",)))
        self.send("Sec-SAP", self.getMessage("test.request",("P2PCDE Originating",)))

        self.listen(self.handle)


    def handle(self, msg, resp_buffer):
        self.LogInfo("Received message of type " + msg.name)
        if(msg.name == "test.request"):
            self.respond(resp_buffer, "test.confirm",("confirm",))
            
        elif(msg.name == "test.confirm"):
            self.LogInfo("CONNECTION TO {} CONFIRMED".format(msg.source))

        else:
            self.LogInfo("Received unknown message type: " + msg.name)