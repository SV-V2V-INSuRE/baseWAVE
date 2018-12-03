from WAVE.SDS import SecureDataService
from WAVE.SSME import StationSecurityManagementEntity
from WAVE.P2PCD import P2PCertDistributionEntity
from service import SAP,Service,Message
from utils.Logger import Logger
import multiprocessing


def startService(s):
    s.start()

if __name__ == '__main__':
    # bootstraps the services
    logger=Logger()
    sds = SecureDataService.SecureDataService(logger=logger)
    ssme = StationSecurityManagementEntity.StationSecurityManagementEntity(logger=logger)
    p2pcde = P2PCertDistributionEntity.P2PCertDistributionEntity(logger=logger)

    # create SAPs
    SSME_Sec_SAP = SAP.SAP("SSME-Sec-SAP")
    SSME_Sec_SAP.bind(sds,ssme)

    SSME_SAP = SAP.SAP("SSME-SAP")
    SSME_SAP.bind(ssme,p2pcde)

    Sec_SAP = SAP.SAP("Sec-SAP")
    Sec_SAP.bind(sds,p2pcde)


    # spawn procs
    procs = []
    services = [sds,ssme,p2pcde]
    for s in services:
        p = multiprocessing.Process(target = startService, args=(s,))
        p.start()
        procs.append(p)

    # wait for services to gracefully end (if they ever do)
    for p in procs:
        p.join()

