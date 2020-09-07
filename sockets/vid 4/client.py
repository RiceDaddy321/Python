import socket
import select
import errno  # match specific error codes
import sys

HEADER_LENGTH = 10

IP = "192.168.1.9"  # change this
PORT = 1234
# setup
my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

# send the above information to the server
Username = my_username.encode('utf-8')
username_header = f"{len(Username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + Username)

while True:
    message = input(f"{my_username} > ")

    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
    try:
        while True:
            # receive things
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):  # didnt get any data
                print("connection close by server")
                sys.exit()

            username_length = int(username_header.decode("utf-8").strip())
            Username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            print(f"{Username} > {message}")

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error', str(e))
            sys.exit()

    except Exception as e:
        print('General Error', str(e))
        sys.exit()
        pass
