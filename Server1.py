import socket
import os
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.43.4",5280))

#message receiver function
def receiv():
	while True:
		msg_in = s.recvfrom(1024)
		msg=msg_in[0].decode()
		if ("bye" in msg.lower()) or ("see you" in msg.lower()) or ("talk to you later" in msg.lower()):
			print("bye")
			os._exit(1)
		print("From "+msg_in[1][0],": ", msg)

#message sender function
def send():
	while True:
		msg_out = input()
		s.sendto(msg_out.encode(),("192.168.43.84",5820))
		if ("bye" in msg_out.lower()) or ("see you" in msg_out.lower()) or ("talk to you later" in msg_out.lower()):
			os._exit(1)

#sender thread
s_thr=threading.Thread(target=send)

#receiver thread
r_thr=threading.Thread(target=receiv)

#starting threads
s_thr.start()
r_thr.start()
