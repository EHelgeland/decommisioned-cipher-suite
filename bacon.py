import argparse

def arg_parse():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('message')
    argparser.add_argument('-c', '--complete', default=False)
    argparser.add_argument('-d', '--decode', default=False)
    return argparser.parse_args()

def binary_to_bacon(string):
    result = []
    for c in string:
        if c == "0":
            result.append("a")
        if c == "1":
            result.append("b")
    return "".join(result)

def convert_to_bacon(message, complete, decode):
    result = []
    for char in message.upper():
        if not complete:
            if char == "J":
                char = "I"
            if char == "V":
                char = "U"
        
        if char == " ":
            c = ord(" ")
        elif char:
            print(ord(char))
            if ord(char) > 86:
                c = ord(char) - 67
            elif ord(char) > 74:
                c = ord(char) - 66
            else:
                c = ord(char) - 65
                
            bin_c = bin(c).replace("0b", "").rjust(5, "0")
            result.append(binary_to_bacon(bin_c))

        else:
            c = ord(char)
    return "".join(result)

def main():
    args = arg_parse()

    result = convert_to_bacon(args.message, args.complete, args.decode)

    print(result)

if __name__ == '__main__':
    main()