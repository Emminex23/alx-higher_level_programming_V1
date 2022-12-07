#!/usr/bin/python3
def uppercase(str):
    strings = " "
    for char in str:
        if (ord(char) >= 97) and (ord(char) <= 122):
            strings += (chr(ord(char) - 32))
        else:
            strings += char
    print("{}".format(strings))
