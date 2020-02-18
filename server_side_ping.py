import socket
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("port", type=int, help="port to bind to socket to")
parser.add_argument("-p", "--protocol", type=str, choices=["UDP", "udp", "TCP", "tcp"],
                    help='The protocol to use for the ping should be taken from : ["UDP", "udp", "TCP","tcp"]')
parser.add_argument("-s", "--size", type=int, help="buffer size. should be grater than 0")
parser.add_argument("-t", "--timeout", type=float, help="timeout for TCP connection should be grater than 0")
args = parser.parse_args()

ip = "localhost"  # we will bind only to local host
port = args.port

if args.protocol and args.protocol in ["TCP", "tcp"]:
    protocol = "TCP"
else:  # if no protocol was specified or UDP protocol was given
    protocol = "UDP"  # default protocol

if args.size:
    if args.size < 0:
        raise (TypeError, "size should be grater than 0")
    size = args.size  # default size

else:
    size = 1024  # if no size was specified or size equals to 0

if args.timeout:
    if args.timeout < 0:
        raise (TypeError, "size should be grater than 0")
    timeout = args.timeout
else:  # if no timeout was specified or timeout equals to 0
    timeout = 10  # default timeout

if protocol == "TCP":
    print("Using TCP")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # set socket for TCP connection
    sock.bind((ip, port))
    sock.listen(True)
    conn, addr = sock.accept()  # will block until the connection will be established
    print('Connection address:', addr)
    while True:
        data = conn.recv(size)
        if not data:  # close the connection when the stream ends
            break
        print("received message : ", str(data, encoding='utf8'))
        conn.send(data)  # echo the given data
    conn.close()

else:  # use UDP protocol
    print("Using UDP")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # set socket for UDP connection
    sock.bind((ip, port))
    while True:
        data, addr = sock.recvfrom(size)
        print("sender address: ", addr)
        print("received message: " + str(data, encoding='utf8'))
