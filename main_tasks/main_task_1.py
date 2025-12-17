#!/usr/bin/env python3
# -*- coding: utf-8 -*-

VOWELS = ('а', 'о', 'у', 'э', 'и', 'ы', 'е', 'ё', 'ю', 'я')

if __name__ == "__main__":
    string = input("Введите строку: ").lower()
    used_letters = set(string)

    used_vowels = []
    for letter in used_letters:
        if letter in VOWELS:
            used_vowels.append(letter)

    print(f"Всего использовано гласных: {len(used_vowels)} ({', '.join(used_vowels)})")
