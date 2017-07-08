PORT = 33333

import sys, time
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

count = 0
while count < 5:
    s.sendto('Hello'.encode(), ('<broadcast>', PORT))
    data, addr = s.recvfrom(1024)
    print('data: ' + data.decode('utf-8') + ' addr: ' + addr[0] + ':' + str(addr[1]))

    count = count + 1

    time.sleep(2)

# Sending the 'stop' will stop the server on the GoPiGo
# s.sendto('stop', addr)
