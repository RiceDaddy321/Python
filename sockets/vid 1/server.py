import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #AF net is ipv4
s.bind((socket.gethostname(), 1234))
s.listen(5)  #queue of 5

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been establish!")
	clientsocket.send(bytes("Welcome to the server", "UTF-8"))  #send to clientsocket