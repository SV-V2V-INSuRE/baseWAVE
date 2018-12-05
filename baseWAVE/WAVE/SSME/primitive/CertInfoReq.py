import enum

class CertIdentifierType(enum.Enum):
    HashedId8 = 1
    HashedId10 = 2

class CertInfoReq:
  def __init__(self, identifierType = CertIdentifierType.HashedId8, identifier = ""):
      self.identifierType = identifierType
      self.identifier = identifier

  def decode(self, content):
      pass
