import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("address", type=str,
                    help="IP address and port to send ping for. the format should be {IP:port}. for example: \
                     127.0.0.1:5000")
parser.add_argument("-m", "--message", type=str, help="message to send with the ping")
parser.add_argument("-p", "--protocol", type=str, choices=["UDP", "udp", "TCP", "tcp"],
                    help='The protocol to use for the ping should be taken from : ["UDP", "udp", "TCP","tcp"]')
parser.add_argument("-s", "--size", type=int, help="buffer size for TCP connection. should be grater than 0")
parser.add_argument("-t", "--timeout", type=float, help="timeout for TCP connection should be be grater than 0")
args = parser.parse_args()

ip = args.address.split(':')[0].strip()  # get the IP address
port = int(args.address.split(':')[1].strip())  # get the port number

if args.message:
    message = args.message
else:
    message = "Hello there!"  # default value for message

if args.protocol and args.protocol in ["TCP", "tcp"]:
    protocol = 'TCP'
else:  # if no protocol was specified or UDP protocol was given
    protocol = 'UDP'  # default protocol

if args.size:
    if args.size < 0:
        raise (TypeError, "size should be grater than 0")
    size = args.size

else:  # if no size was specified or size equals to 0
    size = 1024  # default size

if args.timeout:
    if args.timeout < 0:
        raise (TypeError, "size should be grater than 0")
    timeout = args.timeout  # if no timeout was specified or timeout equals to 0
else:
    timeout = 10  # default timeout

print("target IP:" + str(ip))
print("target port:" + str(port))
print("message : " + str(message))

if protocol == 'TCP':
    print("Using TCP")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # set socket for TCP connection
    sock.settimeout(timeout)  # set timeuot
    sock.connect((ip, port))
    sock.send(bytes(message, encoding='utf8'))
    data = sock.recv(size)
    print("TCP received data:" + str(data, encoding='utf8'))
    sock.close()

else:  # use UDP protocol
    print("Using UDP")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # set socket for UDP connection
    sock.sendto(bytes(message, encoding='utf8'), (ip, port))
