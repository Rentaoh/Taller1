import socket
import os, os.path
import time
import json

sockfile = "./communicate.sock"

if os.path.exists( sockfile ):
  os.remove( sockfile )

print ("Opening socket...")

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
server.bind(('127.0.0.1', 9100))
server.listen(5)

print ("Listening...")
while True:
  conn, addr = server.accept()

  print ("accepted connection")

  while True: 

    data = conn.recv( 1024 )
    if not data:
        break
    else:
        print ("-" * 20)
        dump = [{'Host':'0.0.0.0:9100','Connection':''}]

        print (json.dumps(data))
        if "DONE" == data:
            break
print ("-" * 20)
print ("Shutting down...")

server.close()
os.remove( sockfile )

print ("Done")