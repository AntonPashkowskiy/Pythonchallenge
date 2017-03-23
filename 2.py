#!/usr/bin/python3

def decrypt_byte_string(byte_string):
    exception_list = [ord(' '), ord('.'), ord('('), ord(')')]
    pre_result_string = bytes([c if c in exception_list else c + 2 for c in byte_string]).decode("utf-8")
    translation_table = str.maketrans("{|", "ab")
    return pre_result_string.translate(translation_table)


def main():
    print(decrypt_byte_string(b"map"))


if __name__ == "__main__":
    main()
