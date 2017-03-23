#!/usr/bin/python3
import urllib.parse, urllib.request
import re


def main():
    base_url_template = "http://www.pythonchallenge.com/pc/def/linkedlist.php?{}"
    nothing_value = 12345

    output_file = open("5.txt", "a")

    for i in range(1, 400):
        params = urllib.parse.urlencode({'nothing': nothing_value})
        binary_data = urllib.request.urlopen(base_url_template.format(params)).read()
        string_data = str(binary_data)
        print(string_data)
        output_file.write(string_data + '\n')
        nothing_value = int(re.findall('[0-9]+', string_data)[0])

    output_file.close()


if __name__ == "__main__":
    main()
