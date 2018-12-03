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
SSME-CertificateInfo.request 9.4.1.1
SSME-CertificateInfo.confirm 9.4.1.2
SSME-AddTrustAnchor.request 9.4.2.1
SSME-AddTrustAnchor.confirm 9.4.2.2
SSME-AddCertificate.request 9.4.3.1
SSME-AddCertificate.confirm 9.4.3.2
SSME-VerifyCertificate.request 9.4.4.1
SSME-VerifyCertificate.confirm 9.4.4.2
SSME-DeleteCertificate.request 9.4.5.1
SSME-DeleteCertificate.confirm 9.4.5.2
SSME-AddHashIdBasedRevocation.request 9.4.6.1
SSME-AddHashIdBasedRevocation.confirm 9.4.6.2
SSME-AddIndividualLinkageBasedRevocation.request 9.4.7.1
SSME-AddIndividualLinkageBasedRevocation.confirm 9.4.7.2
SSME-AddGroupLinkageBasedRevocation.request 9.4.8.1
SSME-AddGroupLinkageBasedRevocation.confirm 9.4.8.2
SSME-AddRevocationInfo.request 9.4.9.1
SSME-AddRevocationInfo.confirm 9.4.9.2
SSME-RevocationInformationStatus.request 9.4.10.1
SSME-RevocationInformationStatus.confirm 9.4.10.2
SSME-P2pcdResponseGenerationService.request 9.4.11.1
SSME-P2pcdResponseGenerationService.confirm 9.4.11.2
SSME-P2pcdResponseGeneration.indication 9.4.12.1
SSME-P2pcdConfiguration.request 9.4.13.1
SSME-P2pcdConfiguration.confirm

## SSME-Sec-SAP Operations
SSME-Sec-ReplayDetection.request 9.5.1.1
SSME-Sec-ReplayDetection.confirm 9.5.1.2
SSME-Sec-IncomingP2pcdInfo.request 9.5.2.1
SSME-Sec-IncomingP2pcdInfo.confirm 9.5.2.2
SSME-Sec-OutgoingP2pcdInfo.request 9.5.3.1
SSME-Sec-OutgoingP2pcdInfo.confirm

## Sec-SAP Operations
Sec-CryptomaterialHandle.request 9.3.1.1
Sec-CryptomaterialHandle.confirm 9.3.1.2
Sec-CryptomaterialHandle-GenerateKeyPair.request 9.3.2.1
Sec-CryptomaterialHandle-GenerateKeyPair.confirm 9.3.2.2
Sec-CryptomaterialHandle-StoreKeyPair.request 9.3.3.1
Sec-CryptomaterialHandle-StoreKeyPair.confirm 9.3.3.2
Sec-CryptomaterialHandle-StoreCertificate.request 9.3.4.1
Sec-CryptomaterialHandle-StoreCertificate.confirm 9.3.4.2
Sec-CryptomaterialHandle-StoreCertificateAndKey.request 9.3.5.1
Sec-CryptomaterialHandle-StoreCertificateAndKey.confirm 9.3.5.2
Sec-CryptomaterialHandle-Delete.request 9.3.6.1
Sec-CryptomaterialHandle-Delete.confirm 9.3.6.2
Sec-SymmetricCryptomaterialHandle.request 9.3.7.1
Sec-SymmetricCryptomaterialHandle.confirm 9.3.7.2
Sec-SymmetricCryptomaterialHandle-HashedId8.request 9.3.8.1
Sec-SymmetricCryptomaterialHandle-HashedId8.confirm 9.3.8.2
Sec-SymmetricCryptomaterialHandle-Delete.request 9.3.8.3
Sec-SymmetricCryptomaterialHandle-Delete.confirm 9.3.8.4
Sec-SignedData.request 9.3.9.1
Sec-SignedData.confirm 9.3.9.2
Sec-EncryptedData.request 9.3.10.1
Sec-EncryptedData.confirm 9.3.10.2
Sec-SecureDataPreprocessing.request 9.3.11.1
Sec-SecureDataPreprocessing.confirm 9.3.11.2
Sec-SignedDataVerification.request 9.3.12.1
Sec-SignedDataVerification.confirm 9.3.12.2
Sec-EncryptedDataDecryption.request 9.3.13.1
Sec-EncryptedDataDecryption.confirm