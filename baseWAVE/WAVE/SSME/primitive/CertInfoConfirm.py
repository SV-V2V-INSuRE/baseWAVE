import enum

class CertConfirmResCode(enum.Enum):
    NotFound = 1
    MultiIdentified = 2
    NotVerified = 3
    VerifiedTrusted = 4

class CertInfoConfirm:
    def __init__(self, resCode, certData = [], geoScope = [],
    lastRecTime = None, nextExpTime = "Unknown", trustAnchor = False, verified = False):
        self.ResCode = resCode
        self.CertData = certData
        self.GeoScope = geoScope
        self.LastRecTime = lastRecTime
        self.NextExpTime = nextExpTime
        self.TrustAnchor = trustAnchor
        self.Verified = verified

    def encode(self):
        return ""
