import socket

def receving_udp_mess():
    UDP_IP = "10.100.102.4"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print("received message: %s" % data)



def receving_tcp_mess():
    TCP_IP = "10.100.102.11"
    TCP_PORT = 5005
    BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connection address:', addr)
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        print("received data:", data.decode('utf_8'))
        data = data.decode('utf_8')
        # print(data)
        data = data.split('\n')
        data_dict = {data[0]: data[1]}
        print(data_dict)
        conn.send('ok'.encode('utf_8'))  # echo
    # conn.close()