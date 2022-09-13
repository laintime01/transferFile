import os
import re
import socket
from datetime import datetime

# TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client connect server bind
client.connect(("localhost", 9999))

# open file
file = open("avatar.png", 'rb')
# os.path get file attribute
file_size = os.path.getsize("avatar.png")

print("file_size-> " + str(file_size).encode().decode())

# send encoded file name to the receiver
# create image name using time
now = datetime.now()
now = now.strftime("%m%d%H%M%S")

ext = str(file.name).split('.')[1]
print(ext)

name = str(now + "." + ext)

print(name)

client.send(name.encode())
# send file size to the receiver
client.send(str(file_size).encode())

data = file.read()
# send all the data
client.sendall(data)
# create a bytes object not a regular str object
client.send(b"<END>")

file.close()
client.close()