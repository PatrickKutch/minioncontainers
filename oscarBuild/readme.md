example usage:

docker run -p 10.166.11.165:5000:3232/udp -it patrickkutch/biff-oscar -t 10.166.11.193:6200

where Marvin/another oscar is listening at 10.166.11.193:6200 and on this box you listen on the 10.166.11.165 interface, UDP port 5000 that maps to port 3232 in the container where Oscar is running
