import socket

host='localhost'
port=8002

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host,port))

sock.send("testing message".encode())
sock.send("OK".encode())

confirmacao = sock.recv(1024)

if confirmacao == b'OK':
    print("mensagem recebida")
else:
    print(confirmacao)