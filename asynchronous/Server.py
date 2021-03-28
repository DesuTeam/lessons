import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(2)

while True:
    conn, addr = sock.accept()

    print('connected:', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data)
    conn.close()

