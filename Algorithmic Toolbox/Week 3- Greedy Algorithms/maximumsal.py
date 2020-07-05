#!/usr/bin/env python3
# -*- coding: utf-8 -*-
num = int(input())
data = [int(i) for i in input().split()]

def maxnum(data):
    maxnumber = []
    while data != []:
        maxdig = 0
        for dig in data:
            if greater_equal(dig, maxdig):
                maxdig = dig
        maxnumber.append(maxdig)
        data.remove(maxdig)
            
    return maxnumber

def greater_equal(dig,maxdig):
    return int(str(dig)+str(maxdig)) >= int(str(maxdig)+str(dig))

print(''.join([str(i) for i in maxnum(data)]))
        

