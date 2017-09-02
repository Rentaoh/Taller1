from socket import *
import os
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('127.0.0.1', 1240))
serverSocket.listen(1);

def parse_headers (data):
  headers = {}
  lines = data.splitlines()
  for l in lines:
    parts = l.split(": ", 1)
    if len(parts) == 2:
      headers[parts[0]] = parts[1]
  headers['code'] = lines[len(lines) - 1]
  return headers

while True:
  print ('Ready to serve...')
  connectionSocket, addr = serverSocket.accept()
  try:
    message = connectionSocket.recv(1024)
    

    filename = message.split()[1]
    print(filename)
    f = open(filename[1:])
    outputdata = f.read()

    #Send one HTTP header line into socket
    connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n')

    #Send the content of the requested file to the client
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i])
    connectionSocket.close()

  except IOError:
    connectionSocket.send('&#72;TTP/1.1 404 File not found') ## this is not working
    connectionSocket.close();