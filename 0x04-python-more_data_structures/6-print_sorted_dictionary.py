#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_dictionary = sorted(a_dictionary.items())
    for k, v in s_dictionary:
        print(f"{k}: {v}")
