import socket
from checksum import checksum as checksum_calculator

def receiver(seq:int, recv_sock:socket):
    try:
        message, address = recv_sock.recvfrom(1024)
    except socket.timeout:
        print("Timeout")
    else:
        if message[16:19] == "ACK":
            checksum = message[:16]
            ack_seq = message[19]
            if checksum_calculator(message[16:]) == checksum.decode() and chr(ack_seq) == str(seq):
                return True
    