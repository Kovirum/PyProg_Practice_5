#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    dictionary = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13
    }

    dict_items = dictionary.items()
    dictionary2 = {}

    for key, value in dict_items:
        dictionary2[value] = key

    print(f"Исходный словарь: {dictionary}")
    print(f"Словарь с измененными местами ключами и значениями: {dictionary2}")
