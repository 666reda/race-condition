#!/usr/bin/python
from threading import Thread
import socket

host = "www.google.com"
cookies = "nothing-yet"
post = "here=is&my=body-{\"some\":\"json\"}"

req = "POST / HTTP/1.1\r\n"
req = req + "Host: "+ host + "\r\n"
req = req + "Cookies: "+ cookies + "\r\n"
req = req + "Connection: close\r\n"
req = req + "Content-Length: "+ str(len(post)) +"\r\n\r\n"
req = req + post


class myThread(Thread):
    def __init__(self, ID, name):
        Thread.__init__(self)
        self.threadID = ID
        self.name     = name
    def run(self):
   	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   	    s.connect((host, 80))
   	    s.send(req)
   	    #s.close()

thread1 = myThread(1, "")
thread2 = myThread(2, "")
thread3 = myThread(3, "")
thread1.start()
thread2.start()
thread3.start()

print("\n[*] 3 requests were sent succesfully")