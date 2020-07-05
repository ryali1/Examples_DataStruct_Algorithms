#!/usr/bin/env python3
# -*- coding: utf-8 -*-

num  = int(input())
x = [int(i) for i in input().split()]
x.sort()
y = [int(i) for i in input().split()]
y.sort()


revenue = sum([x[i]*y[i] for i in range(num)])
print(revenue)