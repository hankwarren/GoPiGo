import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


for i in range(5):
    client.sendto('hello', ('255.255.255.255',33333))
    data, addr = client.recvfrom(1024)
    print("received message: %s %s"%(data, addr))


