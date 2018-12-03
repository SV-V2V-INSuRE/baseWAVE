## Overview
This project implements 3 services: the SDS, SSME, P2PCDE.

### Starting the program
run start.py with python 3

### Service Class
The Service class contains several methods that will be helpful in managing a service

### Adding a Method to a Service
To add a method, modify the handle method to handle a message type. In the below example, there are 2 message types handled: test.request and test.confirm.
```
    def handle(self, msg, resp_buffer):
        self.LogInfo("Received message of type " + msg.name)
        if(msg.name == "test.request"):
            self.respond(resp_buffer, "test.confirm",("confirm",))

        elif(msg.name == "test.confirm"):
            self.LogInfo("CONNECTION TO {} CONFIRMED".format(msg.source))
            
        else:
            self.LogInfo("UNKNOWN MESSAGE: " + msg.name)     
```

You may additionally want to add checks to make sure that the call is comming from the correct SAP.

#SAP Operations
## SSME-SAP operations
SSME-CertificateInfo.request 
SSME-CertificateInfo.confirm 
SSME-AddTrustAnchor.request 
SSME-AddTrustAnchor.confirm 
SSME-AddCertificate.request 
SSME-AddCertificate.confirm 
SSME-VerifyCertificate.request 
SSME-VerifyCertificate.confirm 
SSME-DeleteCertificate.request 
SSME-DeleteCertificate.confirm 
SSME-AddHashIdBasedRevocation.request 
SSME-AddHashIdBasedRevocation.confirm 
SSME-AddIndividualLinkageBasedRevocation.request 
SSME-AddIndividualLinkageBasedRevocation.confirm 
SSME-AddGroupLinkageBasedRevocation.request 
SSME-AddGroupLinkageBasedRevocation.confirm 
SSME-AddRevocationInfo.request 
SSME-AddRevocationInfo.confirm 
SSME-RevocationInformationStatus.request 
SSME-RevocationInformationStatus.confirm 
SSME-P2pcdResponseGenerationService.request 
SSME-P2pcdResponseGenerationService.confirm 
SSME-P2pcdResponseGeneration.indication 
SSME-P2pcdConfiguration.request 
SSME-P2pcdConfiguration.confirm

## SSME-Sec-SAP Operations
SSME-Sec-ReplayDetection.request 
SSME-Sec-ReplayDetection.confirm 
SSME-Sec-IncomingP2pcdInfo.request 
SSME-Sec-IncomingP2pcdInfo.confirm 
SSME-Sec-OutgoingP2pcdInfo.request 
SSME-Sec-OutgoingP2pcdInfo.confirm

## Sec-SAP Operations
Sec-CryptomaterialHandle.request 
Sec-CryptomaterialHandle.confirm 
Sec-CryptomaterialHandle-GenerateKeyPair.request 
Sec-CryptomaterialHandle-GenerateKeyPair.confirm 
Sec-CryptomaterialHandle-StoreKeyPair.request 
Sec-CryptomaterialHandle-StoreKeyPair.confirm 
Sec-CryptomaterialHandle-StoreCertificate.request 
Sec-CryptomaterialHandle-StoreCertificate.confirm 
Sec-CryptomaterialHandle-StoreCertificateAndKey.request 
Sec-CryptomaterialHandle-StoreCertificateAndKey.confirm 
Sec-CryptomaterialHandle-Delete.request 
Sec-CryptomaterialHandle-Delete.confirm 
Sec-SymmetricCryptomaterialHandle.request 
Sec-SymmetricCryptomaterialHandle.confirm 
Sec-SymmetricCryptomaterialHandle-HashedId8.request 
Sec-SymmetricCryptomaterialHandle-HashedId8.confirm 
Sec-SymmetricCryptomaterialHandle-Delete.request 
Sec-SymmetricCryptomaterialHandle-Delete.confirm 
Sec-SignedData.request 
Sec-SignedData.confirm 
Sec-EncryptedData.request 
Sec-EncryptedData.confirm 
Sec-SecureDataPreprocessing.request 
Sec-SecureDataPreprocessing.confirm 
Sec-SignedDataVerification.request 
Sec-SignedDataVerification.confirm 
Sec-EncryptedDataDecryption.request 
Sec-EncryptedDataDecryption.confirm