import socket

print("Servidor HTTP")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 9100))
s.listen(1)

while True:
    client_connection, client_address = s.accept()
    
    print("Cliente conectado desde: ", client_address)
    
    print('hola')
    client_connection.send("HTTP/1.1 200 OK")
    client_connection.close()
    
    

