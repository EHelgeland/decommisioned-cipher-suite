import argparse


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('n')
    parser.add_argument('message')
    return parser.parse_args()

def rotate(chars, n):
    # Rotate chars
    result = []
    for char in chars:

        if char == " ":
            c = ord(" ")

        elif char.isupper():
            c = (((ord(char) - 64) + int(n)) % 26) + 64

        elif char.islower():
            c = (((ord(char) - 96) + int(n)) % 26) + 96

        else:
            c = ord(char)

        result.append(chr(c))

    return "".join(result)

def main():
    args = arg_parse()
    
    print(rotate(args.message, args.n))

if __name__ == '__main__':
    main()
