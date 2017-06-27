import gopigo
import socket
import sys
import time
import os
import netifaces

def init():
    global speed
    global servo_position
    global autopilot
    global distance
    speed = 100
    servo_position = 90

    gopigo.set_speed(speed)
    gopigo.enable_servo()
    gopigo.servo(servo_position)
    time.sleep(0.1)
    gopigo.disable_servo()
    autopilot = False
    distance = gopigo.us_dist(15)
    time.sleep(0.1)
    gopigo.enc_tgt(1,1,0)

def remote(data, address):
    global speed
    global servo_position
    global autopilot
    global distance

    print(data)
    command = data.split(' ')
    length = len(command)

    print(str(len(command)) + ': ' + command[0])

    if command[0] == 'forward':
        print('going forward')
        #distance = gopigo.us_dist(15)
        #time.sleep(0.1)
        #gopigo.enc_tgt(1, 1, distance)
        gopigo.fwd()

    elif command[0] == 'backward':
        gopigo.bwd()

    elif command[0] == 'left':
        gopigo.left()

    elif command[0] == 'right':
        print('go right')
        gopigo.right()
        print('went right')

    elif command[0] == 'rotl':
        gopigo.left_rot()

    elif command[0] == 'rotr':
        gopigo.right_rot()

    elif command[0] == 'home':
        servo_position = 90
        print('point home', servo_position)
        gopigo.enable_servo()
        gopigo.servo(servo_position)
        time.sleep(0.1)
        gopigo.disable_servo()

    elif command[0] == 'sleft':
        servo_position = servo_position + 10
        if servo_position > 180:
            servo_position = 180

        print('point left', servo_position)
        gopigo.enable_servo()
        gopigo.servo(servo_position)
        time.sleep(0.1)
        gopigo.disable_servo()

    elif command[0] == 'sright':
        servo_position = servo_position - 10
        if servo_position < 0:
            servo_position = 0
        print('point right', servo_position)
        gopigo.enable_servo()
        gopigo.servo(servo_position)
        time.sleep(0.1)
        gopigo.disable_servo()

    elif command[0] == 'stop':
        gopigo.stop()

    elif command[0] == 'speed':
        print('speed: ' + command[1])
        gopigo.set_speed(int(command[1]))
        speed = int(command[1])

    elif command[0] == 'incspeed':
        speed = speed + 10
        if speed > 255:
            speed = 255
        gopigo.increase_speed()

    elif command[0] == 'decspeed':
        speed = speed - 10
        if speed < 35:      # a practical limit?
            speed = 35
        gopigo.decrease_speed()

    elif command[0] == 'startauto':
        # look for distance to obstacle
        # move a couple of inches
        #autopilot()
        autopilot = True
        print(command[0] + ' ' + str(autopilot))

    elif command[0] == 'stopauto':
        # stop
        autopilot = False
        print(command[0] + ' ' + str(autopilot))

    elif command[0] == 'sayip':
        ipAddr = netifaces.ifaddresses('wlan0')[2][0]['addr']
        print('say ip address')
        os.system('flite -t "' + str(ipAddr) + '"')

    elif command[0] == 'showlidar':
        # generate lidar map
        # send the map to the requester
        pass

    elif command[0] == 'kill':
        os.system('flite -t "Exiting the server"')
        return False

    elif command[0] == 'encoder':
        print('encoder: ' + str(len(command)))
        print('  encoder: ' + command[1])
        gopigo.enc_tgt(1, 1, int(command[1]))
        gopigo.fwd()

    elif command[0] == 'rencoder':
        print('rencoder: ' + command[1])
        gopigo.enc_tgt(0, 1, int(command[1]))
        gopigo.fwd()

    elif command[0] == 'lencoder':
        print('lencoder: ' + command[1])
        gopigo.enc_tgt(1, 0, int(command[1]))
        gopigo.fwd()

    elif command[0] == 'distance':
        distance = gopigo.us_dist(15)
        print('distance: ' + str(distance) + ' cm')
        string = '{0} centimeters'.format(distance)

        os.system('flite -t "{0}"'.format(string))
    else:
        if len(command) == 1:
            print('unknown: ' + command[0])
        else:
            print(command[0] + ' for ' + command[1] + 'seconds')

        time.sleep(0.1)

    return True

