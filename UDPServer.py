import socket
import struct
from checksum import checksum as checksum_calculator

SEGMENT_SIZE = 16

source_port = 1111
destination_port = 1112
host = '127.0.0.1'
receiver_addr = (host, destination_port)
this_addr = (host, source_port)

socket_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock.bind(this_addr)
recv_sock.settimeout(1)

seq = 0

while True:
    offset = 0
    content = input()
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