# Listen for a broadcast and send the apps IP address.

from socket import *
import netifaces as ni

serverAddress = ('', 33333)

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(serverAddress)

while True:
    data, addr = serverSocket.recvfrom(1024)

    if data == 'stop':
        print('Client wants me to stop')
        break
    else:
        ipAddr = ni.ifaddresses('wlan0')[2][0]['addr']
        serverSocket.sendto(str(ipAddr), addr)

serverSocket.close()

