import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1', 9100))
try:
	
	while True:
		data = data.recv(1024)
		print(data)
finally:
	sock.close()