import socket
import os
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.43.84",5820))

# function to receive message
def receive():
    while True:
        msg_in=s.recvfrom(1024)
        msg=msg_in[0].decode()
        if ("bye" in msg.lower()) or ("see you" in msg.lower()) or ("talk to you later" in msg.lower()):
            print("bye")
            os._exit(1)
        print("From "+ msg_in[1][0]+" : ", msg)

# function to send message
def send():
    while True:
        msg_out=input()
        s.sendto(msg_out.encode(),("192.168.43.4",5280))
        if ("bye" in msg_out.lower()) or ("see you" in msg_out.lower()) or ("talk to you later" in msg_out.lower()):
            os._exit(1)

#sender & receiver thread
r_thr=threading.Thread(target=receive)
s_thr=threading.Thread(target=send)

#starting thread
r_thr.start()
s_thr.start()

