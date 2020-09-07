import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF net is ipv4
s.bind((socket.gethostname(), 1234))
s.listen(5)  # queue of 5

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been establish!")

    d = {1: "Hey", 2: "There"}
    msg = pickle.dumps(d)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "UTF-8") + msg
    print(msg)

    clientsocket.send(msg)  # send to clientsocket
