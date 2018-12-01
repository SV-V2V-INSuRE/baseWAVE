import WAVE.SDS.SecureDataService as SecureDataService


if __name__ == '__main__':
    # bootstraps the instance
    sds = SecureDataService.SecureDataService()

    sds.start(0,0)

