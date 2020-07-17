import socket

HOST = "127.0.0.1"
PORT = 3000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as socket:
     socket.bind((HOST,PORT))
     print("SOCKET BINDED SUCCESFULLY WITH THE SERVER")
     socket.listen()
     print("Socket status ====== listening")
     connection, address = socket.accept()
     with connection:                            #the with statement is like try and finally only + it will even close the connection once code is executed completely
         print(address)
         while 1:
            data = connection.recv(1024)
            if not data:
               print(data)                 # empty bytes object is sent when a connection is closed from client side
               print("Disconnected")
               break
            else:
                connection.sendall(data)

