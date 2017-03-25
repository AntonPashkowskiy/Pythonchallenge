#!/usr/bin/python3
import re
from zipfile import ZipFile


def main():
    next_file_number = 90052
    log_file = open('7.txt', 'w')
    comment_file = open('7_comment.txt', 'w')
    channel_zip = ZipFile('channel.zip')

    while True:
        filename = str(next_file_number) + '.txt'
        nothing_file = channel_zip.open(filename)
        nothing_file_info = channel_zip.getinfo(filename)

        file_text = nothing_file.read().decode('utf-8')
        file_comment = nothing_file_info.comment.decode('utf-8')

        log_file.write(file_text + '\n')
        comment_file.write(file_comment)

        next_file_number = int(re.findall('[0-9]+', file_text)[0])

        nothing_file.close()

    channel_zip.close()
    comment_file.close()
    log_file.close()


if __name__ == '__main__':
    main()
