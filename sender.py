import socket
import struct
from receiver import receiver
from checksum import checksum as checksum_calculator

SEGMENT_SIZE = 16

def sender(content:str, send_socket:socket, recv_sock:socket, source_port:int, destination_port:int, receiver_addr:int):
    seq = 0
    offset = 0
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

            send_socket.sendto(packet_with_header, receiver_addr)

            ack_received = True if receiver(seq, recv_sock) else False

        seq = 1 - seq