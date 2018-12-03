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