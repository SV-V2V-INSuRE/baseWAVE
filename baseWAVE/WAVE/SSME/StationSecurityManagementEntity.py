from utils import Database
from service import Service,SAP,Message
from WAVE.SSME.primitive import CertInfo, AddAnchor, AddCert, VerifyCert

class StationSecurityManagementEntity(Service.Service):
    def __init__(self, logger=None):
        Service.Service.__init__(self, name = "SSME", logger=logger)
        self.db = Database.Database()

    #assume SAPs are already bound
    def start(self):
        #send test messages
        self.send("SSME-Sec-SAP", self.getMessage("test.request",("SSME Originating",)))
        self.listen(self.handle)


    def handle(self, msg, resp_buffer):
        self.LogInfo("Received message of type " + msg.name)
        if(msg.name == "test.request"):
            self.respond(resp_buffer, "test.confirm",("confirm",))

        elif(msg.name == "test.confirm"):
            self.LogInfo("CONNECTION TO {} CONFIRMED".format(msg.source))
        elif(msg.name == "SSME-CertificateInfo.request"):
            req = CertInfo.CertInfoReq().decode(msg.content)
            # TODO
            pass
        elif(msg.name == "SSME-AddTrustAnchor.request"):
            req = AddAnchor.AddAnchorReq().decode(msg.content)
            self.db.saveCert(req.Certificate)
            conf = AddAnchor.AddAnchorConfirm(AddAnchor.AddAnchorResCode.Success)

            pass
        elif(msg.name == "SSME-AddCertificate.request"):
            req = AddCert.AddCertReq().decode(msg.content)
            self.db.saveCert(req.Certificate)
            conf = AddCert.AddCertConfirm(AddCert.AddCertResCode.Success)

            pass
        elif(msg.name == "SSME-VerifyCertificate.request"):
            req = VerifyCert.VerifyCertReq().decode(msg.content)
            # TODO
            pass
        elif(msg.name == "SSME-DeleteCertificate.request"):
            pass
        elif(msg.name == "SSME-AddHashIdBasedRevocation.request"):
            pass
        elif(msg.name == "SSME-AddIndividualLinkageBasedRevocation.request"):
            pass
        elif(msg.name == "SSME-AddGroupLinkageBasedRevocation.request"):
            pass
        elif(msg.name == "SSME-AddRevocationInfo.request"):
            pass
        elif(msg.name == "SSME-RevocationInformationStatus.request"):
            pass
        elif(msg.name == "SSME-P2pcdResponseGenerationService.confirm"):
            pass
        elif(msg.name == "SSME-P2pcdResponseGeneration.indication"):
            pass
        elif(msg.name == "SSME-P2pcdConfiguration.confirm"):
            pass
        elif(msg.name == "SSME-Sec-ReplayDetection.request"):
            pass
        elif(msg.name == "SSME-Sec-IncomingP2pcdInfo.request"):
            pass
        elif(msg.name == "SSME-Sec-OutgoingP2pcdInfo.request"):
            pass


        else:
            self.LogInfo("UNKNOWN MESSAGE: " + msg.name)
