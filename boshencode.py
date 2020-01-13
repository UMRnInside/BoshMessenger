import boshdata
import struct

BFCAP = 12
BFMASK = (2 ** BFCAP) - 1

def byte2_split(ibytes):
    "little-endian! returns a tuple like (11, 4095)"
    ibytes += b"\0\0"
    # Packing unsigned short int, should be 2-byte 
    num = struct.unpack(b"<H", ibytes[0:2])[0]
    ret1 = num & 0x0F # 4-bit
    ret2 = (num >> 4) 
    return (ret1, ret2)

def gen_length_indicator(length):
    "The length indicator is in little-endian."
    if length >= 2**(16):
        raise ValueError("Too long! Ensure your data is shorter than " + str(2**(BCAP*2)))
    sps = byte2_split(struct.pack("<I", length))
    return boshdata.bosh[sps[0]] + boshdata.fortunes[sps[1]]

def bytes_encode(bdata):
    for curbyte in iter(bdata):
        pass

if __name__ == "__main__":
    print(gen_length_indicator(42))
