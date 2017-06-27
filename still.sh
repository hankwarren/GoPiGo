raspistill --nopreview -w 320 -h 240 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 6000000 -th 0:0:0 &
# These setings work OK. The mmal driver reports lots of skipped frames.
#
# To finnaly get this to work I did:
#
# cd work/MJPG-streamer/mjpg-streamer
# sudo cp mjpg_streamer /user/local/bin
# sudo cp output_http.so input_file.so /usr/local/lib
# sudo cp -R www /usr/local/www

