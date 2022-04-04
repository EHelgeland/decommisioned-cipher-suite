import argparse

def arg_parse():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('message')
    argparser.add_argument('-c', '--complete', dest='complete', action='store_const', const=True, default=False, help='Use complete alphabet (default: U=V, I=V)')
    argparser.add_argument('-d', '--decode', dest='decode', action='store_const', const=True, default=False, help='Decode the message (default: Encode)')
    return argparser.parse_args()

def binary_to_bacon(string):
    result = []
    for c in string:
        if c == "0":
            result.append("a")
        if c == "1":
            result.append("b")
    return "".join(result)

def bacon_to_binary(string):
    result = []
    for c in string:
        if c == "a":
            result.append("0")
        if c == "b":
            result.append("1")
    return "".join(result)

def convert_to_bacon(message, complete):
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
            if not complete:
                if ord(char) > 86:
                    c = ord(char) - 67
                elif ord(char) > 74:
                    c = ord(char) - 66
                else:
                    c = ord(char) - 65
            else:
                c = ord(char) - 65
                
            bin_c = bin(c).replace("0b", "").rjust(5, "0")
            result.append(binary_to_bacon(bin_c))

        else:
            c = ord(char)
    return "".join(result)

def convert_from_bacon(message, complete):
    binary_string = bacon_to_binary(message)
    binary_list = []
    for i in range(0, len(binary_string), 5):
        binary_list.append(binary_string[i:i+5])
    
    result = []
    for bin_char in binary_list:
        int_char = int(bin_char, 2)
        if not complete:
            if int_char > 19:
                c = chr(int_char + 67)
            elif int_char > 8:
                c = chr(int_char + 66)
            else:
                c = chr(int_char + 65)
        else:
            c = chr(int_char + 65)
        result.append(c)
    return "".join(result)



def main():
    args = arg_parse()
    if args.decode:
        result = convert_from_bacon(args.message, args.complete)
    else:
        result = convert_to_bacon(args.message, args.complete)

    print(result)

if __name__ == '__main__':
    main()