#!/usr/bin/python

import socket
import sys

if len(sys.argv) == 4:
    type = sys.argv[1]
    host = sys.argv[2]
    sport = int(sys.argv[3])
    eport = sport + 1
elif len(sys.argv) == 5:
    type = sys.argv[1]
    host = sys.argv[2]
    sport = int(sys.argv[3])
    eport = int(sys.argv[4]) + 1
else:
    print "portcheck.py <udp/tcp> <host> <port>"
    exit()

if type == 'udp':
    for port in range(sport, eport):
        udpdata = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        send_msg = 'Test Message'
        udpdata.sendto(send_msg, (host, port))
        print str(type) + ' ' + str(host) + ':' + str(port) + ' OK'

elif type == 'tcp':
    for port in range(sport, eport):
        try:
            tcpdata = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
            tcpdata.settimeout(1)
            tcpdata.connect((host,port))
            print str(type) + ' ' + str(host) + ':' + str(port) + ' OK'
            tcpdata.close()
        except:
            print "port error"

else:
    print "udp or tcp"
