import socket
import time
# header: notify the program about the length of the message and other things

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF net is ipv4
s.bind((socket.gethostname(), 1234))
s.listen(5)  # queue of 5

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been establish!")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    print(msg)

    clientsocket.send(bytes(msg, "UTF-8"))  # send to clientsocket

    while True:
        time.sleep(3)
        msg = f"The time is: {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "UTF-8"))
