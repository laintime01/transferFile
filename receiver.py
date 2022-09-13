import tqdm
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

conn, addr = server.accept()

file_name = conn.recv(1024).decode("utf-8","ignore")
file_size = conn.recv(1024).decode("utf-8","ignore")

#
# print("Creating file with new name : " + file_name)
# print("And file size is :" + file_size)


file = open(file_name, "wb")
file_bytes = b""

done = False

progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000,
                     total=float(file_size))

while not done:
    data = conn.recv(1024)
    # use file_bytes not data coz sometime we may receive <E
    # ND> data like this
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes += data

file.write(file_bytes)
file.close()
conn.close()
server.close()
