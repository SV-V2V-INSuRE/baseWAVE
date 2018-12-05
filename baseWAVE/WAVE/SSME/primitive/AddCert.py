import enum

class AddCertReq:

  def __init__(self, certificate = "", verified = True):
      self.Certificate = certificate
      self.verified = verified

  def decode(self, content):
      pass

class AddCertResCode(enum.Enum):
    Success = 1
    Invalid = 2

class AddCertConfirm:
    def __init__(self, resCode):
        self.ResCode = resCode

    def encode(self):
        return ""
