import argparse
import re

import binascii


def print_strings(file_obj, encoding, min_len):
    # Right now all this function does is print its arguments.
    # You'll need to replace that code with code that actually finds and prints the strings!

    binary_list = []

    if encoding == "s":
        mode = "UTF-8"
    elif encoding == "l":
        mode = "UTF-16-le"
    elif encoding == "b":
        mode = "UTF-16-be"

    for block in iter(lambda: file_obj.read(16), b''):
        raw_byte = binascii.hexlify(block)
        byte_array = re.sub('(..)', r'\1 ', raw_byte.decode(mode)).split()
        binary_list.append(byte_array)

    string = ""

    # utf-8 length 2
    for bit_list in binary_list:
        for bit in bit_list:
            if 32 <= int(bit, 16) <= 126:
                string += chr(int(bit, 16))
            else:
                if len(string) >= min_len:
                    print(string)
                    string = ""
                else:
                    string = ""
        if len(string) >= min_len:
            print(string)
            string = ""
        else:
            string = ""


def main():
    parser = argparse.ArgumentParser(description='Print the printable strings from a file.')
    parser.add_argument('filename')
    parser.add_argument('-n', metavar='min-len', type=int, default=4,
                        help='Print sequences of characters that are at least min-len characters long')
    parser.add_argument('-e', metavar='encoding', choices=('s', 'l', 'b'), default='s',
                        help='Select the character encoding of the strings that are to be found. ' +
                             'Possible values for encoding are: s = UTF-8, b = big-endian UTF-16, ' +
                             'l = little endian UTF-16.')
    args = parser.parse_args()

    with open(args.filename, 'rb') as f:
        print_strings(f, args.e, args.n)


if __name__ == '__main__':
    main()
