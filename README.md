Run

    udp-server
    
on the GoPiGo.


---------------------------------------------------------
The http server is nginx. The pages are at /srv/www. 


---------------------------------------------------------
sudo pip install netifaces

---------------------------------------------------------
To start the servers on boot up.

sudo crontab -e

add:
    @reboot sh /home/pi/work/flask/launcher.sh >/home/pi/logs/cronlog 2>&1
    @reboot sh /home/pi/work/flask/ip-server.sh >/home/pi/logs/cronlog 2>&1
    @reboot sh /home/pi/work/flask/bt-server.sh >/home/pi/logs/cronlog 2>&1

chmod 755 launcher.sh
chmod 755 ip-server.sh

---------------------------------------------------------
Bluetooth

To make the pi discoverable do:
    sudo hciconfig hci0 piscan

then, doing sudo hciconfig -a
    you should find

        UP RUNNING PSCAN ISCAN

I was able to pair from my phone and from the laptop.

make sure the following are installed
    sudo apt-get install bluetooth
    sudo apt-get install bluez
    sudo apt-get install python-bluez

To show if bluetooth is up...
    sudo service bluetooth status

Added
    hciconfig hci0 piscan

    to /etc/rc.local

    Put this line just before the exit 0. This makes the gopigo
    discoverable on boot up.


Created file /etc/machine-info with content

    PRETTY_HOSTNAME=speedbump1

    to change the discoverable name for the pi.

Another way to change the name temporarily is

    sudo hciconfig hci0 name 'speedbump1'

hciconfig -a
    shows the bluetooth configuration information. Use this to
    figure out if bluetooth is even up and if it is discoverable.

In the server, use port 0.

Android uses the advertise machinery, so had to add this to my script.
Part of that is to use port 0 which results in the next available port.
Next load the Serial Port Profile:

    sudo sdptool add SP

And then run the Bluetooth daemon in 'compatibility' mode. To do that:

    edit /etc/systemd/system/dbus-org.bluez.service

    In the line with 'bluetoothd' add -C after 'bluetoothd'. Reboot.

