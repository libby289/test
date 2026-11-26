import socket
socket_client=socket.socket()
socket_client.connect(('127.0.0.1',8080))
while True:
    msg=input("请输入消息:").encode('utf-8')
    socket_client.send(msg)
    data=socket_client.recv(1024).decode('utf-8')
    print("服务端发来的消息：",data)
    if msg=="exit":
        break
socket_client.close()