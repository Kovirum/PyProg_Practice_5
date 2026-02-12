#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")

    A = {'a', 'b', 'f', 'g', 'i'}
    B = {'c', 'f', 'g', 'i', 's', 'v'}
    C = {'a', 'g', 'h', 'i'}
    D = {'f', 'w', 'x'}

    X = (A.intersection(B)).union(C)
    Y = (A.intersection(u.difference(B)).union(C.difference(B)))

    print(f"{X=}")
    print(f"{Y=}")
