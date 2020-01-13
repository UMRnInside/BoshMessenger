import boshdata
import struct

BCAP = 12
BMASK = (2 ** BCAP) - 1

def byte3_split(ibytes):
    "little-endian! returns a tuple like (11, 4095)"
    ibytes += b"\0\0\0"
    # Packing unsigned int, should be 4-byte 
    num = struct.unpack(b"<I", ibytes[0:3] + b"\0")[0]
    ret1 = num & BMASK
    ret2 = (num >> BCAP) & BMASK
    return (ret1, ret2)

def gen_length_indicator(length):
    "The length indicator is in little-endian."
    if length >= 2**(BCAP * 2):
        raise ValueError("Too long! Ensure your data is shorter than " + str(2**(BCAP*2)))
    sps = byte3_split(struct.pack("<I", length))
    return tuple(map(lambda i: boshdata.fortunes[i], sps) )

def bytes_encode(bdata):
    for curbyte in iter(bdata):
        pass

if __name__ == "__main__":
    print(gen_length_indicator(103))
