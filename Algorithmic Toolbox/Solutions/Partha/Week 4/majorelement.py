#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num = int(input())
sequence = [int(i) for i in input().split()]

def divide(sequence, left, right):
    if left + 1 == right:
        return sequence[left]
    elif left + 2 == right:
        return sequence[left]
    mean = (left+right)//2
    l = divide(sequence,left,mean)
    r = divide(sequence, mean, right)
    
    k1, k2 = 0,0
    for i in sequence[left:right]:
        if i == l:
            k1 += 1
        elif i == r:
            k2 += 1
    if k1 > (right - left)//2 and l != -1:
        return l
    elif k2 > (right-left)//2 and r != -1:
        return r
    else:
        return -1

print(int(divide(sequence, 0, num) != -1))