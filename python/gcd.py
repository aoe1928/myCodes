#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 最小公倍数の計算
def gcd(n1:int, n2:int):
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1%n2)

if __name__ == "__main__":
    print(gcd(120, 180))