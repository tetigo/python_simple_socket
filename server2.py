import os
import socket

host='localhost'
port=8002

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((host,port))

sock.listen(5)

while True:
    novoSock, _ = sock.accept()
    nomeArquivo = novoSock.recv(1024).decode()
    novoArquivo = novoSock.recv(1000000000)
    try:
        with open(f'arquivos/{nomeArquivo}.png', 'wb') as arq:
            arq.write(novoArquivo)
    except FileNotFoundError:
        os.mkdir('arquivos')
        novoSock.send(b'deu problema na geracao, tente novamente')
        
    else: novoSock.send(b'OK')