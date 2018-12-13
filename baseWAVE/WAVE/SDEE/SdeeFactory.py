import SDEE

class SdeeFactory:
    def __init__(self):
        self.num_id=0

        
    def generateSdee(self):
        self.num_id += 1
        return SDEE.SDEE(self.num_id)  