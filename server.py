import socket

host='localhost'
port=8002

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((host,port))

sock.listen(5)

while True:
    novoSock, _ = sock.accept()
    msg = novoSock.recv(1024).decode()
    if(msg == b'OK'):
        novoSock.send(b'OK')
    else:
        novoSock.send(b'NAO ENTENDI')
    print(msg)