#!/usr/bin/env python3
# -*- coding: utf-8 -*-
num = int(input())
data = []

for _ in range(num):
    y,z  = [int(i) for i in input().split()]
    data.append((y,z))
    
data.sort(key = lambda x: x[1])

ind = 0
coor = []

while ind < num:
    currentind= data[ind]
    while ind < num-1 and currentind[1] >= data[ind+1][0]:
        ind += 1
    coor.append(currentind[1])
    ind += 1
print(len(coor))
print(' '.join([str(i) for i in coor]))

