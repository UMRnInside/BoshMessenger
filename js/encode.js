function byte2_encode(inum)
{
    lpart = inum & 0x0F;
    hpart = inum >> 4;
    return bosh[lpart] + fortunes[hpart];
}

function gen_length_indicator(length)
{
    if (length >= 65536)
    {
        throw "Too large!";
    }
    return byte2_encode(length);
}

function boshEncode(text)
{
    var URIFormat = encodeURIComponent(text);
    var ret = "　　", tmp = "";
    ret += gen_length_indicator(URIFormat.length / 3);

    // Prevent Index-out-of-Range
    URIFormat += "%00%00"
    while (URIFormat.length >= 6)
    {
        var unit = URIFormat.substr(0, 6).replace(/%/g, "");
        // after parseInt, newbytes are BIG-endian
        // what we're expecting are LITTIE-endian ones
        var newbytes = parseInt(unit, 16);
        newbytes = ((newbytes & 0xFF) << 8) | (newbytes >> 8);

        var newtext = byte2_encode(newbytes);

        tmp += newtext;
        if ((tmp.length > 175 && Math.random() < 0.07) || tmp.length > 416)
        {
            ret += tmp;
            // full-width spaces
            ret += '\n　　';
            tmp = "";
        }
        URIFormat = URIFormat.substr(6);
    }
    if (tmp.length > 0)
    {
        ret += tmp;
    }
    return ret;
}
