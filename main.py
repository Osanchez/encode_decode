

def encode(codepoint):
    if codepoint < 128:
        return bytes([codepoint])

    elif 128 <= codepoint <= 2047:
        byte_left = 0b11000000 | (0b00000000000 | codepoint) >> 6
        print(bin(byte_left))
        byte_right = 0b10000000 | (0b00000000000 | codepoint)
        print(bin(byte_right))
        print([byte_left, byte_right])
        return bytes([byte_left, byte_right])

    elif 2048 <= codepoint <= 4095:
        byte_left = 0b11100000 | (0b0000000000000000 | codepoint) >> 12
        print(bin(byte_left))
        byte_middle = 0b10000000 | (0b0000000000000000 | codepoint) >> 6
        print(bin(byte_middle))
        byte_right = 0b10000000 | (0b0000000000000000 | codepoint) << 12
        print(bin(byte_right))
        print([byte_left, byte_middle, byte_right])
        #return bytes([byte_left, byte_middle, byte_right])


def decode(bytes_object):
    if len(bytes_object) == 1:
        return bytes_object[0]


def main():
    print(encode(163))
    print()
    print(encode(2090))


if __name__ == "__main__":
    main()

