# helper methods for IOInterface
import os
import uuid

def write_new_file(dir, message):
    newfile_name = os.path.join(dir, generate_uuid())
    write_file(newfile_name, message)


def write_file(path, message):
    
    with open(path,"w+") as file:
        file.write(message)


def read_file(path, delete_on_completion=True):
    content = ""
    with open(path,"r") as file:
        content = file.read()

    if(delete_on_completion):
        os.remove(path)

    return content


def create_directory(path):
    os.mkdir(path)

def remove_directory(path):
    os.rmdir(path)

def generate_uuid():
    return str(uuid.uuid1())