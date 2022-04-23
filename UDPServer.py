from audioop import add
import socket
import struct
import binascii

SEGMENT_SIZE = 16

def checksum_calculator(data):

    data = bin(int(binascii.hexlify(data),16))
   
    c1 = data[0:16] or '0'
    c2 = data[16:32] or '0'
    c3 = data[32:48] or '0'
    c4 = data[48:64] or '0'
 
    Sum = bin(int(c1, 2)+int(c2, 2)+int(c3, 2)+int(c4, 2))[2:]

    if(len(Sum) > 16):
        x = len(Sum)-16
        Sum = bin(int(Sum[0:x], 2)+int(Sum[x:], 2))[2:]
    if(len(Sum) < 16):
        Sum = '0'*(16-len(Sum))+Sum
 
    Checksum = ''
    for i in Sum:
        if(i == '1'):
            Checksum += '0'
        else:
            Checksum += '1'
    return Checksum


def check_checksum_calculator(data, checksum):
   
    data = bin(int(binascii.hexlify(data),16))
    checksum = bin(int(binascii.hexlify(bytes(checksum)),16))

    c1 = data[0:16] or '0'
    c2 = data[16:32] or '0'
    c3 = data[32:48] or '0'
    c4 = data[48:64] or '0'
 
    ReceiverSum = bin(int(c1, 2)+int(c2, 2)+int(checksum, 2) +
                      int(c3, 2)+int(c4, 2)+int(checksum, 2))[2:]

    if(len(ReceiverSum) > 16):
        x = len(ReceiverSum)-16
        ReceiverSum = bin(int(ReceiverSum[0:x], 2)+int(ReceiverSum[x:], 2))[2:]
 
    return int(ReceiverSum, 2) == 0

with open("teste.txt") as f:
    content = f.read()


source_port = 1111
destination_port = 1112
receiver_addr = ('127.0.0.1', destination_port)
this_addr = ('127.0.0.1', source_port)

socket_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock.bind(this_addr)
recv_sock.settimeout(1)

offset = 0
seq = 0

while offset < len(content):
    if offset + SEGMENT_SIZE > len(content):
        segment = content[offset:]
    else:
        segment = content[offset:offset + SEGMENT_SIZE]

    offset += SEGMENT_SIZE - seq

    ack_received = False

    while not ack_received:
        packet = (str(seq) + segment).encode()
        data_length = len(packet)
        checksum = checksum_calculator(packet)
        udp_header = struct.pack('!IIIII', source_port, destination_port, data_length, int(checksum, 2), seq)

        packet_with_header = udp_header + packet

        socket_object.sendto(packet_with_header, receiver_addr)

        try:
            message, address = recv_sock.recvfrom(1024)

        except socket.timeout:
            print("Timeout")
        else:
            checksum = message[:16]
            ack_seq = message[19]
            if checksum_calculator(message[16:]) == checksum.decode() and chr(ack_seq) == str(seq):
                ack_received = True

    seq = 1 - seq

socket_object.close()
