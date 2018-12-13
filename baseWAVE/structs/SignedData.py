class HashAlgorithm(Enum):
    sha256=0

class HeaderInfo:
    def __init__(self, psid, generationTime, expiryTime, generationLocation):
        self.psid = psid
        self.generationTime = generationTime
        self.expiryTime = expiryTime
        self.generationLocation = generationLocation


class SignedDataPayload:
    def __init__(self, data = None, extDataHash = None):
        if not data and not extDataHash:
            raise ValueError('Need either a data or extDataHash')

        self.data = data
        self.extDataHash = extDataHash


class ToBeSignedData:
    def __init__(self, payload, headerInfo):
        self.payload = payload
        self.headerInfo = headerInfo


class SignedData:
    def __init__(self, hashId, tbsData, signer, signature):
        self.hashId=hashId
        self.tbsData = tbsData
        self.signer=signer
        self.signature = signature