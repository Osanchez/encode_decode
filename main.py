

def encode(codepoint):
    if codepoint < 128:
        print([codepoint])
        return bytes([codepoint])

    elif 128 <= codepoint <= 2047:
        byte_left = (0b110 << 5) | (0b11111000000 & codepoint) >> 6
        byte_right = (0b10 << 6) | (0b00000111111 & codepoint)
        print([byte_left, byte_right])
        return bytes([byte_left, byte_right])

    elif 2048 <= codepoint <= 65535:
        byte_left = (0b1110 << 4) | (0b1111000000000000 & codepoint) >> 12
        byte_middle = (0b10 << 6) | (0b0000111111000000 & codepoint) >> 6
        byte_right = (0b10 << 6) | (0b0000000000111111 & codepoint)
        print([byte_left, byte_middle, byte_right])
        return bytes([byte_left, byte_middle, byte_right])

    elif 65536 <= codepoint <= 1114111:
        byte_outer_left = (0b11110 << 3) | (0b111000000000000000000 & codepoint) >> 18
        byte_inner_left = (0b10 << 6) | (0b000111111000000000000 & codepoint) >> 12
        byte_inner_right = (0b10 << 6) | (0b000000000111111000000 & codepoint) >> 6
        byte_outer_right = (0b10 << 6) | (0b000000000000000111111 & codepoint)
        print([byte_outer_left, byte_inner_left, byte_inner_right, byte_outer_right])
        return bytes([byte_outer_left, byte_inner_left, byte_inner_right, byte_outer_right])



def decode(bytes_object):
    if len(bytes_object) == 1:
        return bytes_object[0]


def main():
    print(encode(122))
    print()
    print(encode(163))
    print()
    print(encode(2048))
    print()
    print(encode(65537))


if __name__ == "__main__":
    main()

