import socket
from checksum import checksum as checksum_calculator
import struct

source_port = 1112
destination_port = 1111
host = '127.0.0.1'

receiver_addr = (host, destination_port)
this_addr = (host, source_port)

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

    if int(checksum_calculator(data), 2) == correct_checksum:
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
