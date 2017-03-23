#!/usr/bin/python3
from collections import Counter


def get_symbols_rate():
    with open("3.txt") as target_file:
        counter_obj = Counter(letter for line in target_file
                                     for letter in line.lower())
        return counter_obj


def print_symbols_rate(counter_obj):
    for key in counter_obj:
        value = counter_obj[key]
        print("{0}: {1}".format(key, str(value)))


def main():
    counter = get_symbols_rate()
    print_symbols_rate(counter)


if __name__ == "__main__":
    main()
