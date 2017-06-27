import bluetooth

bd_addr = '00:1A:7D:DA:71:13'
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
sock.send('hello!')
sock.close()

