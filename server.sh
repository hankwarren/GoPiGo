MJPG=/opt/mjpg-streamer
echo $MJPG
raspistill -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 -n &
LD_LIBRARY_PATH=$MJPG/ /opt/mjpg-streamer/mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -p 9000 -w /opt/mjpg-streamer/www" &

# To look at the network stuff (ports and such)
#   sudo lsof -i
#   sudo netstat -lptu
#   sudo netstat -tulpn

