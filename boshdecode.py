import boshdata
import struct
import io

BFCAP = 12
BFMASK = (2 ** BFCAP) - 1

def byte2_unpack(numtuple):
    "little-endian! receives a tuple like (11, 4095) and return corrosponding bytes"
    num = numtuple[0] | (numtuple[1] << 4)
    # Packing unsigned short int, should be 2-byte 
    return struct.pack(b"<H", num)

def byte2_decode(utf8string):
    ret1, ret2, truncated = 0, 0, 0

    # Bosh comes first
    for i in range(0, len(boshdata.bosh)):
        pattern = boshdata.bosh[i]
        if utf8string.startswith(pattern):
            ret1 = i
            truncated += len(pattern)
            utf8string = utf8string[len(pattern):]
            break
    # Fortune
    for j in range(0, len(boshdata.fortunes)):
        pattern = boshdata.fortunes[j]
        if utf8string.startswith(pattern):
            ret2 = j
            truncated += len(pattern)
            break
    return byte2_unpack((ret1, ret2)), truncated


def decode_length_indicator(utf8seq):
    "The length indicator is in little-endian."
    rawbytes, truncated = byte2_decode(utf8seq)
    datalen = struct.unpack("<H", rawbytes)[0]
    return datalen, truncated

def utf8_decode(utf8data):
    iobuffer = io.BytesIO(b"")
    datalen, dl_trunc = decode_length_indicator(utf8data)
    utf8data = utf8data[dl_trunc:]

    while utf8data and iobuffer.tell() < datalen:
        obytes, truncated = byte2_decode(utf8data)
        utf8data = utf8data[truncated:]
        iobuffer.write(obytes)

    iobuffer.seek(0)
    return iobuffer.read(datalen)
        

if __name__ == "__main__":
    import sys
    #print(byte2_unpack((0x01, 0x626)))
    #print(byte2_decode("带着这些问题, 我们来审视一下x。爱迪生曾经说过，天才是百分之一的勤奋加百分之九十九的汗水。这不禁令我深思。"))
    desc_stdout = sys.stdout.fileno()
    st_in = sys.stdin.read()
    open(desc_stdout, "wb", closefd=False).write(utf8_decode(st_in))
    #sys.stdout.write(bytes_encode(st_in))

