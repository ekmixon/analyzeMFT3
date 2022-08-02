# This is all Willi Ballenthin's. Saved me a lot of headaches

def parse_little_endian_signed_positive(buf):
    return sum(b * (1 << (i * 8)) for i, b in enumerate(buf))

def parse_little_endian_signed_negative(buf):
    ret = sum((b ^ 0xFF) * (1 << (i * 8)) for i, b in enumerate(buf))
    ret += 1

    ret *= -1
    return ret

def parse_little_endian_signed(buf):
    return (
        parse_little_endian_signed_negative(buf)
        if buf[-1] & 0b10000000
        else parse_little_endian_signed_positive(buf)
    )