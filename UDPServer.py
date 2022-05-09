import socket
from checksum import checksum as checksum_calculator
import struct
from receiver import receiver
from sender import sender
from datetime import datetime
from chatbot.main import option


now = datetime.now().strftime("%H:%M")

source_port = 1112
destination_port = 1111
host = '127.0.0.1'

recv_addr = (host, destination_port)
this_addr = (host, source_port)

send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_sock.bind(this_addr)
recv_sock.settimeout(1)

answer = ''

while answer != "Digite sair para sair":
    expecting_seq = 0

    while True:
        try:
            message, address = recv_sock.recvfrom(1024)
        except socket.timeout:
            continue
        else:
            if message[16:19].decode() != "ACK":
                udp_header = message[:20]
                data = message[20:]
                udp_header = struct.unpack("!IIIII", udp_header)
                correct_checksum = udp_header[3]

                seq = udp_header[4]
                content = data[1:]
                

                if int(checksum_calculator(data), 2) == correct_checksum:
                    value = "ACK" + str(seq)
                    checksum = checksum_calculator(value.encode())
                    send_socket.sendto((checksum + value).encode(), recv_addr)
                    if str(seq) == str(expecting_seq):
                        answer = option(content, address)
                        expecting_seq = 1 - expecting_seq
                        break
                else:
                    negative_seq = 1 - expecting_seq
                    checksum = checksum_calculator(negative_seq)
                    header = struct.pack("!II", int(checksum, 2), negative_seq)
                    send_socket.sendto(header, recv_addr)
                    break

    sender(answer, send_socket, recv_sock, source_port, destination_port, recv_addr)
send_socket.close()