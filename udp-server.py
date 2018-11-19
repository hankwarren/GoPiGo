import gopigo
import socket
import sys
import time
import os
import netifaces
from autopilot import *
from remote import *
import alsaaudio as audio

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setblocking(1)

# use '0.0.0.0' or ''
server_address = ('0.0.0.0', 8000)
print('starting up on %s port %s' % server_address)

sock.bind(server_address)

init()

mixer = audio.Mixer('PCM')
mixer.setvolume(85)
#os.system('flite -t "wifi started."')

running = True
while running:
    data, address = sock.recvfrom(1024)
    running = remote(data, address)

    if data:
        print('data: ' + data)
        sent = sock.sendto(data, address)

sock.close()

