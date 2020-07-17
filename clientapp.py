import socket

PORT=3000
HOST="127.0.0.1"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    while 1:
        a=input("enter the message : ")
        if(a=="exit" or a=="EXIT"):
            break
        socket.sendall(a.encode('ASCII'))
        data = socket.recv(1024)
        print("message received",data.decode('ASCII'))
