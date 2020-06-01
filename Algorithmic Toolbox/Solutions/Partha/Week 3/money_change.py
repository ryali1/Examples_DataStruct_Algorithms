#!/usr/bin/env python3
# -*- coding: utf-8 -*-


x = int(input())
temp = 0
for i in [10,5,1]:
    if x>=i:
        change = x//i
        temp += change
        x = x%i
        if x == 0:
            print(temp)
            quit()