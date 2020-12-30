import socket
from socket import *



def sending_udp_mess(UDP_IP):
    # UDP_IP = "10.100.102.4"
    UDP_PORT = 5005
    #sending
    MESSAGE = ('0xfeedbeef'+'0x2'+str(UDP_PORT))
    MESSAGE = bytes(MESSAGE,'utf-8')

    # sock = socket.socket(socket.AF_INET, # Internet
    #                      socket.SOCK_DGRAM) # UDP
    # sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

    cs = socket(AF_INET, SOCK_DGRAM)
    cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    cs.sendto(MESSAGE, ('255.255.255.255', UDP_PORT))


def sending_tcp_mess():
    TCP_IP = "10.100.102.11"
    TCP_PORT = 5005
    BUFFER_SIZE = 1024
    MESSAGE = "Hello".encode('utf_8')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print("received data:", data.decode('utf_8'))