class Ieee1609Dot2Content:
    def __init__(self, unsecuredData="", signedData=False, encryptedData=False, signedCertificateRequest=False):
        self.signedData=signedData
        self.encryptedData=encryptedData
        self.signedCertificateRequest=signedCertificateRequest