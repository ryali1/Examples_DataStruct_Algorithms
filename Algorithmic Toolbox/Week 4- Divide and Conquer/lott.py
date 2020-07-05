#!/usr/bin/env python3
# -*- coding: utf-8 -*-

main = list()
s, p = [int(i) for i in input().split()]

for i in range(s):
    x, y = [int(i) for i in input().split()]
    main.append((x,'mark1'))
    main.append((y,'mark2'))
    
point = input().split()
for i in point:
    main.append((int(i),'p'))
    
main.sort()

segment = 0
pointsegdict = dict()
for i in main:
    if i[1] == 'mark1': segment += 1
    elif i[1] == 'mark2': segment -= 1
    else: 
        pointsegdict[i[0]] = segment

fill = ''
for i in point:
    fill += str(pointsegdict[int(i)]) + ' '
print(fill[:-1])
