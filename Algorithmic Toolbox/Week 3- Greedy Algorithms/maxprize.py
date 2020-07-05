#!/usr/bin/env python3
# -*- coding: utf-8 -*-
num = int(input())
if num == 1:
    print(1)
    print(1)
    quit()

x = num

prize = []
for i in range(1,num):
    if x > 2*i:
        prize.append(i)
        x -= i
    else:
        prize.append(x)
        break

print(len(prize))
print(' '.join([str(i) for i in prize]))