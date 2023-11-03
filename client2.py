import socket

host='localhost'
port=8002

arquivo = open('thumb.png', 'rb')

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host,port))

nome = input("nome do arquivo")

sock.send(nome.encode())
sock.send(arquivo.read())

confirmacao = sock.recv(1024)

print(confirmacao)