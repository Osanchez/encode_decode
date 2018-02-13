

def encode(codepoint):
    if codepoint < 128:
        x = codepoint % 16
        if x == 0:
        return codepoint


def decode(bytes_object):
    if len(bytes_object) == 1:
        return bytes_object[0]


def main():
    print(encode(127))

if __name__ == "__main__":
    main()

