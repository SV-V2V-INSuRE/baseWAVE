# encode object to message content
# decode message content to object

class AbstractEncoder:

    @abstractmethod
    def encode(obj):
        return ""

    @abstractmethod
    def decode(str):
        return ""
