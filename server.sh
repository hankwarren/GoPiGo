MJPG=/usr/local/lib
echo $MJPG
LD_LIBRARY_PATH=$MJPG/ mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -w /usr/local/www"

# To look at the network stuff (ports and such)
#   sudo lsof -i
#   sudo netstat -lptu
#   sudo netstat -tulpn

