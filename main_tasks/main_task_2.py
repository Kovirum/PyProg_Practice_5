#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    string1 = input("Введите первую строку: ")
    string2 = input("Введите вторую строку: ")

    string1_letters = set(string1)
    string2_letters = set(string2)

    common_letters = []

    for string1_letter in string1_letters:
        if string1_letter in string2_letters:
            common_letters.append(string1_letter)

    print(f"Общих символов в строках: {len(common_letters)} ({', '.join(common_letters)})")
