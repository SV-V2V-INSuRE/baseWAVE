from service.BasicService import BasicService

class SecureDataService:
    def __init__(self):
        # set up event handler
        self.service = BasicService()

    def start(self, SmeeSecSap, SecSap):
        self.SmeeSecSap = SmeeSecSap
        self.SecSap = SecSap

        method_dict = {
            "generateSPDU": self.generateSPDU,
            "verifySignedSPDU": self.verifySignedSPDU,
            "decryptSPDU": self.decryptSPDU
        }

        self.service.listen(method_dict)


    def generateSPDU(self, caller, params):
        pass

    def verifySignedSPDU(self, caller, params):
        pass

    def decryptSPDU(self, caller, params):
        pass
    
