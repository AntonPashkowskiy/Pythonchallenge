#!/usr/bin/python3
import re


def main():
    with open("4.txt") as target_file:
        data = target_file.read()
        print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))


if __name__ == "__main__":
    main()
