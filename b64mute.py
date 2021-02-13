import base64
import argparse
from random import randrange

parser = argparse.ArgumentParser(description='Base64 Mutator')
parser.add_argument('-d', dest='indata', help='Input data (string)')
parser.add_argument('-f', dest='infile', help='Input file')
parser.add_argument('-o', dest='outfile', help='Output file')

def doEncode(mBytes):
    b64Bytes = base64.b64encode(mBytes)
    return b64Bytes

def openFile(filename):
    with open(filename, "rb") as f:
        fileobj = f.read()
    return fileobj

if __name__ == '__main__':
    args    = parser.parse_args()
    indata  = args.indata
    infile  = args.infile
    outfile = args.outfile

    outmsg = b'' # This will hold the base64 object

    if indata:
        data2enc = indata
        data2enc_bytes = data2enc.encode('utf-8') # Convert to bytes object
    elif infile:
        data2enc = openFile(infile)
        data2enc_bytes = data2enc # It's already a bytes object here

    msgLen = len(data2enc_bytes)
    x = 0
    while x < msgLen:
        chunkSize = randrange(1,4)
        outmsg += doEncode(data2enc_bytes[x:x+chunkSize])
        x = x + chunkSize
    if outfile: # We write to file 
        f = open(outfile, 'wb')
        f.write(outmsg)
        f.close()
    else: # Otherwise write to stdout
        b64Enc = outmsg.decode('utf-8')
        print("{}".format(b64Enc))

