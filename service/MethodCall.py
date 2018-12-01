class MethodCall:
    def __init__(self, caller, method, params):
        self.caller = caller
        self.method = method
        self.params = params