#!/usr/bin/python

import bluetooth
import os
import remote
import gopigo
import syslog
import time

syslog.syslog('Starting bt-server.py')

serverSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

#port = bluetooth.get_available_port(bluetooth.RFCOMM)
port = 1
serverSocket.bind(("", port))
serverSocket.listen(1)
syslog.syslog('advertise_service ==============================')

time.sleep(1)

bluetooth.advertise_service(serverSocket,
        "GoPiGo Serial Port",
        service_classes=[bluetooth.SERIAL_PORT_CLASS],
        profiles=[bluetooth.SERIAL_PORT_PROFILE])

os.system('flite -t "Bluetooth started."')

while True:
    syslog.syslog('Bluetooth started. ===============================')
    clientSocket, address = serverSocket.accept()

    remote.init()

    #os.system('flite -t "Bluetooth connected."')

    running = True
    while running:
        try:
            data = clientSocket.recv(1024)
            running = remote.remote(data, address)

            if data:
                syslog.syslog('bt-server.py - data: ' + data + ' ' + str(remote.distance))
                sent = clientSocket.send(data + ' ' + str(remote.distance) + ' cm')

        except bluetooth.btcommon.BluetoothError as e:
            print('connection reset: {0}: {1}'.format(e.errno, e.strerror))
            break;

    clientSocket.close()
    #os.system('flite -t "Connection reset"')

    syslog.syslog('exited connection, listen for another +++++++++++++++++++++++++++')

serverSocket.close()

