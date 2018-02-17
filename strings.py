import argparse


def print_strings(file_obj, encoding, min_len):
    string = ""

    if encoding == 's':
        byte = file_obj.read(1)
        while byte:
            value = int.from_bytes(byte, byteorder='big')
            if 32 <= value <= 126:
                string += chr(value)
            else:
                if len(string) >= min_len:
                    print(string)
                    string = ""
                else:
                    string = ""
            byte = file_obj.read(1)
        if len(string) >= min_len:
            print(string)
            string = ""
    elif encoding == 'b':
        byte = file_obj.read(2)
        while byte:
            value = int.from_bytes(byte, byteorder='big')
            if 32 <= value <= 126:
                string += chr(value)
            else:
                if len(string) >= min_len:
                    print(string)
                    string = ""
                else:
                    string = ""
            byte = file_obj.read(2)
        if len(string) >= min_len:
            print(string)
            string = ""
    elif encoding == 'l':
        byte = file_obj.read(2)
        while byte:
            value = int.from_bytes(byte, byteorder='little')
            if 32 <= value <= 126:
                string += chr(value)
            else:
                if len(string) >= min_len:
                    print(string)
                    string = ""
                else:
                    string = ""
                byte = file_obj.read(2)
        if len(string) >= min_len:
            print(string)
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
