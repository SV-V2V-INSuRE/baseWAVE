import enum

class VerifyCertReq:

  def __init__(self, certificate = None, SPDU = None):
      self.Certificate = certificate
      self.SDPU = SPDU

  def decode(self, content):
      pass

class VerifyCertResCode(enum.Enum):
    Verified = 1
    NoAnchor = 2
    Revoked = 3

class VerifyCertConfirm:
    def __init__(self, resCode):
        self.ResCode = resCode

    def encode(self):
        return ""
