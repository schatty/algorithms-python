"""
Decode huffman encoding into original string.
First line contains number of unique symbols in original
string and length of encoded string, following lines
contain letter: code info. Output original decoded string.
"""


def main():
    k, l = list(map(int, input().split()))
    codes_dict = {}
    for _ in range(k):
        sym, code = list(input().split(':'))
        codes_dict[sym.strip()] = code.strip()
    encoded_string = input()
    code2sym = {v: k for k, v in codes_dict.items()}

    decoded_string = ''
    cur_code = ''
    for i in range(l):
        cur_code += encoded_string[i]
        if cur_code in code2sym:
            decoded_string += code2sym[cur_code]
            cur_code = ''
    print(decoded_string)


if __name__ == "__main__":
    main()
