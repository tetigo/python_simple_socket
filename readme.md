# Simple tests with socket

### test1 - Send and receives message (simple bot)

Open 2 terminals.

The first one, run "python server.py"

The second one, run "python client.py"

In the client, we send a message and receives a message back. If message is "OK", then receives "mensagem recebida" back, otherwise receives the own message back.

### test2 - Send name of file and the own file (png) to be received in the server and saved there

Open 2 terminals.

The first one, run "python server2.py"

the second one, run "python client2.py"

In the client you will be asked to enter the name of the file png that you wanna send to the server.

In the example, we already have "thumb.png" to play with.

The file will be saved in the root path under the "arquivos" directory.

