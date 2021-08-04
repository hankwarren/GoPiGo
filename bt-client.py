import bluetooth
serverMACAddress = 'B8:27:EB:FA:8C:08'

port = 0
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))

while True:
    text = input()
    if text == "quit":
        break
    s.send(bytes(text, 'UTF-8'))

s.close()