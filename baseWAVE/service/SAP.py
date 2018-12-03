from .Buffer import Buffer
import time, multiprocessing

class SAP:
    def __init__(self, name):
        self.InBuffer = Buffer()
        self.OutBuffer = Buffer()
        self.name = name
        self.bind_count=0


    def bind(self, service1, service2):
        service1.bindSAP(self)
        service2.bindSAP(self, reverse_flow=True)


#used for testing
def _test1(sap):
    sap.InBuffer.write("hi")
    print(sap.OutBuffer.read())


def _test2(sap):
    print(sap.InBuffer.read())
    sap.OutBuffer.write("bye")


#test functionality
if __name__ == '__main__':
    sap = SAP("test")

    # spawn tests
    p1 = multiprocessing.Process(target = _test1, args=(sap,))
    p1.start()
    p2 = multiprocessing.Process(target = _test2, args=(sap,))
    p2.start()

    p1.join()
    p2.join()

