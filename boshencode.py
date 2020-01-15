import boshdata
import struct
import random
import io

BFCAP = 12
BFMASK = (2 ** BFCAP) - 1

def byte2_pack(ibytes):
    "little-endian! returns a tuple like (11, 4095)"
    ibytes += b"\0\0"
    # Packing unsigned short int, should be 2-byte 
    num = struct.unpack(b"<H", ibytes[0:2])[0]
    ret1 = num & 0x0F # 4-bit
    ret2 = (num >> 4) 
    return (ret1, ret2)

def byte2_encode(ibytes):
    rets = byte2_pack(ibytes)
    return boshdata.bosh[rets[0]] + boshdata.fortunes[rets[1]]

def gen_length_indicator(length):
    "The length indicator is in little-endian."
    if length >= 2**(16):
        raise ValueError("Too long! Ensure your data is shorter than " + str(2**(BCAP*2)))
    sps = byte2_pack(struct.pack("<I", length))
    return boshdata.bosh[sps[0]] + boshdata.fortunes[sps[1]]

def bytes_encode(bdata):
    iobuffer = io.StringIO("")
    tmp = ""
    lenindi = gen_length_indicator( len(bdata) )
    iobuffer.write(lenindi)

    for curbytes in ( bdata[i:i+2] for i in range(0, len(bdata), 2) ):
        tmp += byte2_encode(curbytes)
        if (len(tmp) > 175 and random.random() < 0.07) or len(tmp) > 416:
            iobuffer.write(tmp)
            iobuffer.write("\n")
            tmp = ""

    iobuffer.seek(0)
    return iobuffer.read()

if __name__ == "__main__":
    import sys
    desc_stdin = sys.stdin.fileno()
    st_in = open(desc_stdin, "rb", closefd=False).read()
    sys.stdout.write(bytes_encode(st_in))

