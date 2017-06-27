import socket
import sys

HOST, PORT = "10.0.0.103", 8000
data = " ".join(sys.argv[1:])

print(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if sys.version_info > (3,):
    sock.sendto(data.encode('UTF-8'), (HOST, PORT))
    received = sock.recv(1024)
    print('Received: ' + received.decode('UTF-8'))
else:
    sock.sendto(data, (HOST, PORT))
    received = sock.recv(1024)
    print('Received: ' + received)

