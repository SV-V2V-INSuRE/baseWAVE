class Certificate:
    def __init__(self, version, issuer, key, signature):
        self.version = version
        self.issuer = issuer
        self.key = key
        self.signature = signature

    def __eq__(self, other):
        return self.version == other.version and \
            self.issuer == other.issuer and \
            self.key == other.key and \
            self.signature == other.signature

    def __hash__(self):
        return hash((self.version, self.issuer, self.key, self.signature))

    def encode():
        return ""
