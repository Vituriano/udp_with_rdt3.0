import binascii

def checksum(data):

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