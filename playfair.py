import argparse
import string

def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('key')
    arg_parser.add_argument('message')
    arg_parser.add_argument('-d', '--decode', dest='decode', action='store_const', const=True, default=False, help='Decode the message (default: Encode)')
    return arg_parser.parse_args()

def make_char_pairs(text):
    text_list = []
    for i in range(0,len(text),2):
        if text[i] == text[i+1]:
            text_list.append(text[i].upper() + 'X')
        else:
            text_list.append(text[i].upper() + text[i+1].upper())
    return text_list

def generate_polybius_square(key):
    key = key.upper()

    # Remove recurring characters
    new_key = ""
    for i in range(len(key)):
        if key[i] not in key[:i]:
            new_key += key[i]

    # Remove key characters from alphabet
    alphatbet = string.ascii_uppercase
    for char in new_key:
        alphatbet = alphatbet.replace(char, '')
    alphatbet = new_key + alphatbet

    # Remove i or j to fit into polybius
    index_of_i = alphatbet.index('I')
    index_of_j = alphatbet.index('J')
    if index_of_i > index_of_j:
        alphatbet = alphatbet.replace('I','')
    else:
        alphatbet = alphatbet.replace('J','')

    key_list = []
    for i in range(0,len(alphatbet),5):
        key_list.append(alphatbet[i:i+5])

    return key_list

def find_index(a, b, polybius):
    for i in range(len(polybius)):
        if a in polybius[i]:
            x = [i, polybius[i].index(a)]

        if b in polybius[i]:
            y = [i, polybius[i].index(b)]
    return x,y

def rotate_row(x, y, polybius):
    if x[1] == 4:
        x[1] = 0
    else:
        x[1] = x[1] + 1
    if y[1] == 4:
        y[1] = 0
    else:
        y[1] = y[1] + 1

    return polybius[x[0]][x[1]], polybius[y[0]][y[1]]

def rotate_column(x, y, polybius):
    if x[0] == 4:
        x[0] = 0
    else:
        x[0] = x[0] + 1
    if y[0] == 4:
        y[0] = 0
    else:
        y[0] = y[0] + 1

    return polybius[x[0]][x[1]], polybius[y[0]][y[1]]

def rotate_row_decode(x, y, polybius):
    if x[1] == 0:
        x[1] = 4
    else:
        x[1] = x[1] - 1
    if y[1] == 0:
        y[1] = 4
    else:
        y[1] = y[1] - 1

    return polybius[x[0]][x[1]], polybius[y[0]][y[1]]

def rotate_column_decode(x, y, polybius):
    if x[0] == 0:
        x[0] = 4
    else:
        x[0] = x[0] - 1
    if y[0] == 0:
        y[0] = 4
    else:
        y[0] = y[0] - 1

    return polybius[x[0]][x[1]], polybius[y[0]][y[1]]

def rotate_square(x, y, polybius):
    return polybius[x[0]][y[1]], polybius[y[0]][x[1]]

def join_tuples(tuples) -> str:
    return ''.join(tuples)

def main():
    args = parse_args()
    message_pairs = make_char_pairs(args.message.replace(' ', ''))
    polybius = generate_polybius_square(args.key)
    output = []

    for p in message_pairs:
        x,y = find_index(p[0], p[1], polybius)
        if x[0] == y[0]:
            if args.decode:
                output.append(rotate_row_decode(x, y, polybius))
            else:
                output.append(rotate_row(x, y, polybius))
        
        elif x[1] == y[1]:
            if args.decode:
                output.append(rotate_column_decode(x, y, polybius))
            else:
                output.append(rotate_column(x, y, polybius))

        else:
            output.append(rotate_square(x, y, polybius))
    print("".join(list(map(join_tuples, output))))

if __name__ == '__main__':
    main()