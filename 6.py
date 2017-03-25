#!/usr/bin/python3
import pickle


def main():
    with open('banner.p', 'rb') as banner_file:
        data = banner_file.read()
        deserialized_data = pickle.loads(data)
        for array in deserialized_data:
            for symbol, count in array:
                print(symbol * count, end = '')
            print()


if __name__ == '__main__':
    main()
