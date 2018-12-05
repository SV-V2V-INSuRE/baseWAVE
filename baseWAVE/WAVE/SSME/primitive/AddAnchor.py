import enum

class AddAnchorReq:

  def __init__(self, certificate = ""):
      self.Certificate = certificate

  def decode(self, content):
      pass

class AddAnchorResCode(enum.Enum):
    Success = 1
    Invalid = 2
    Revoked = 3
    Unverified = 4

class AddAnchorConfirm:
    def __init__(self, resCode):
        self.ResCode = resCode

    def encode(self):
        return ""
