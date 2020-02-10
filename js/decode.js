function byte2_decode(text)
{
    // returns URIComponent like "%AA%BB"
    var component, truncated = 0;
    var lpart = -1, hpart = -1;
    text = text.trim();

    // Bosh comes first
    for (lpart in bosh)
    {
        var pattern = bosh[lpart];
        if (text.startsWith(pattern))
        {
            truncated += pattern.length;
            text = text.substr(pattern.length);
            break;
        }
    }
    // Fortunes
    for (hpart in fortunes)
    {
        var pattern = fortunes[hpart];
        if (text.startsWith(pattern))
        {
            truncated += pattern.length;
            text = text.substr(pattern.length);
            break;
        }
    }
    //console.log(lpart + " " + hpart);
    var combined = (hpart << 4) | lpart;
    var hexcomb = combined.toString(16);
    hexcomb = "0000".substr(0, 4-hexcomb.length) + hexcomb;
    component = "%" + hexcomb.substr(0, 2) + "%" + hexcomb.substr(2, 2);

    return [component, truncated];
}

function decode_length_indicator(text)
{
    var comp_trunc = byte2_decode(text);
    var length = parseInt(comp_trunc[0].replace(/%/g, ""), 16);
    return [length, comp_trunc[1] ];
}

function boshDecode(text)
{
    // trim() cannot remove full-width spaces
    text = text.replace(/[　]/g, "").replace(/[ ]/g, "");
    var length_trunc = decode_length_indicator(text);
    var datalen = length_trunc[0];
    var decodedURI = ""
    text = text.substr(length_trunc[1]);

    while (text.length > 0 && decodedURI.length < datalen * 3)
    {
        text = text.trim();
        var comp_trunc = byte2_decode(text);
        // got BIG-endian, transform into LITTLE-endian
        decodedURI += comp_trunc[0].substr(3, 3) + comp_trunc[0].substr(0, 3);
        text = text.substr(comp_trunc[1]);
    }
    return decodedURI.substr(0, datalen*3);
}
