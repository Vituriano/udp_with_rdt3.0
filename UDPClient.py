import socket
import zlib
import struct
import binascii

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
    if(len(ReceiverSum) < 16):
        ReceiverSum = '0'*(16-len(ReceiverSum))+ReceiverSum
 
    return int(ReceiverSum, 2) == 0

source_port = 1112
destination_port = 1111
receiver_addr = ('127.0.0.1', destination_port)
this_addr = ('127.0.0.1', source_port)

send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock.bind(this_addr)

expecting_seq = 0

while True:
    full_packet, sender_address = recv_sock.recvfrom(1024)

    udp_header = full_packet[:20]
    data = full_packet[20:]
    udp_header = struct.unpack("!IIIII", udp_header)
    correct_checksum = udp_header[3]

    seq = udp_header[4]
    content = data[1:]

    is_data_corrupted = check_checksum_calculator(data, correct_checksum)

    if not is_data_corrupted:
        value = "ACK" + str(seq)
        checksum = checksum_calculator(value.encode())
        send_socket.sendto((checksum + value).encode(), receiver_addr)
        if str(seq) == str(expecting_seq):
            print(content.decode())
            expecting_seq = 1 - expecting_seq
    else:
        negative_seq = 1 - expecting_seq
        checksum = checksum_calculator(negative_seq)
        header = struct.pack("!II", int(checksum, 2), negative_seq)
        send_socket.sendto(header, receiver_addr)
