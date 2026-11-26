import socket
socket_server = socket.socket()
socket_server.bind(('127.0.0.1', 8080))
socket_server.listen(5)

conn, addr = socket_server.accept()
print("连接成功")
while True:
    data = conn.recv(1024).decode('utf-8')
    print("客户端发来的消息：",data)
    msg=input("请输入回复:").encode('utf-8')
    if msg=="exit":
        break
    conn.send(msg)
conn.close()