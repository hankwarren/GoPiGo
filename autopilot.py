import gopigo
import socket
import time

def autopilot(sock):
    while True:
        distance = gopigo.us_dist(15)
        print('distance: ' + str(distance))
        enc_tgt(1, 1, distance)
        gopigo.fwd()

        while distance > 0:
            distance = gopigo.read_enc_status()

            ready = select.select([sock], [], [], 0.5)
            if ready[0]:
                data, address = sock.recvfrom(1024)

                command = data.split(' ')
                if command[0] == 'stopauto':
                    break


        if enc == 0:
            pass
            # turn and try again

# get distance to obstacle
# start moving
# monitor for autostop and check the progress

# when we get to the obstacle, turn right
#   find distance to obstatcle and start over
