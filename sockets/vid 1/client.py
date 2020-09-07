import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF net is ipv4
s.connect((socket.gethostname(), 1234))

msg = s.recv(1024)  # our buffer is 1024 bytes
print(msg.decode("utf-8"))
