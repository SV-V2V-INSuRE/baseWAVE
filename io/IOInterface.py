# handles sending and receiving messages to/from lower layer protocols
import IOHelper
import os

class IOInterface:

    def __init__(self, base_path):
        #ensure base path exists
        if not os.path.exists(base_path):
            IOHelper.create_directory(base_path)

        #make instance paths
        self.inst_path = os.path.join(base_path, IOHelper.generate_uuid())
        self.in_path = os.path.join(self.inst_path,"in")
        self.out_path = os.path.join(self.inst_path,"out")


    def __del__(self):
        #need to clean up paths
        IOHelper.remove_directory(self.inst_path)


    def send(self, msg):
        IOHelper.write_new_file(self.out_path, msg)


    def recv(self):
        #get a message
        return IOHelper.read_file(os.listdir(self.in_path)[0], delete_on_completion=True)
        

    def recv_queue_empty(self):
        return len(os.listdir(self.in_path) == 0)