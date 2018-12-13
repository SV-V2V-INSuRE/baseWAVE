from service.Message import Message
from Crypto.Cipher import AES

class CryptomaterialState(Enum):
    Initialized=0
    Key_Pair_Only=1
    Key_And_Certificate=1

class SymCryptoAlgorithm(Enum):
    ecdsaBrainpoolP256r1WithSha256 = 0
    ecdsaNistP256WithSha256 = 1
    eciesNistp256 = 2
    eciesBrainpoolP256r1 = 3


class CryptomaterialType(Enum):
    KeyPair = 0

class DataEncryptionKeyType(Enum):
    Static=0
    Ephemeral=1

class DataType(Enum):
    Iee1609Dot2Data=0
    Raw=1

class ECPointFormat(Enum):
    Compressed=0
    Uncompressed=1

class Cryptomaterial:
    def __init__(self):
        self.state = CryptomaterialState.Initialized

class EncryptionResponseCode(Enum):
    Success = 0
    IncorrectInputs = 1
    FailOnSomeCertificates = 2
    FailOnAllCertificates = 3

class CryptomaterialHandler:
    def __init__(self):
        self.num_handles=0
        self.CryptomaterialArray = []

    def getCryptomaterial(self, handle):
        return self.CryptomaterialArray[handle]


    def getNewHandle(self):
        # todo more random handles
        new_handle = len(self.num_handles)
        
        self.CryptomaterialArray.append(Cryptomaterial())

        return new_handle
    

    def storeKeyPair(self, handle, algorithm, public_key, private_key):
        self.CryptomaterialArray[handle].algorithm = algorithm
        self.CryptomaterialArray[handle].state = CryptomaterialState.Key_Pair_Only

        self.CryptomaterialArray[handle].public_key = public_key
        self.CryptomaterialArray[handle].public_key = private_key


    def storeCertificate(self, handle, certificate, private_key):
        self.CryptomaterialArray[handle].state = CryptomaterialState.Key_And_Certificate
        self.CryptomaterialArray[handle].certificate = certificate
        self.CryptomaterialArray[handle].private_key = private_key


    def getNewSymmetricHandle(self, algorithm):
        new_handle = self.getNewHandle()
        self.CryptomaterialArray[new_handle].algorithm = algorithm
        return new_handle


    def encryptData(self, data, dataType, dataEncKeyType,SymCHMs = None, RecipientCerts = None, SignedDataRecipientInfo = None, RespEncKey = None, EncKeyType=None, ECPointFormat= None):
        #encrypt using passed keys
        encrypted = None

        if SymCHMs:
            # we only support AES-CCM
            if (dataEncKeyType == DataEncryptionKeyType.Static):
                cipher = AES.new(key, AES.MODE_CCM)

                if dataType == DataType.Raw:
                    encrypted = cipher.encrypt(data)

                else:
                    # TODO
                    pass
            else # Ephemeral
                # TODO
                pass


        elif RecipientCerts:
            pass


        elif SignedDataRecipientInfo:
            if (ECPointFormat == None):
               raise ValueError('Incorrect Inputs')
            
            # TODO

        elif RespEncKey:
            pass

        else:
            raise ValueError('Incorrect Inputs')
        
        return encrypted


    def decrypt(data, chmHandle, signedDataRecipientInfo) :
        chm = getCryptomaterial(chmHandle)

        # we will assume AES-CCM / raw, for now
        cipher = AES.new(key, AES.MODE_CCM)

        if dataType == DataType.Raw:
            encrypted = cipher.encrypt(data)


        
    
    