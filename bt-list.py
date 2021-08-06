import bluetooth, os, time, syslog

nearby_devices = bluetooth.discover_devices(duration=4,
                                lookup_names=True,
                                flush_cache=True,
                                lookup_class=False)

print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print(" {} - {}".format(name, addr))