#!/usr/bin/env python3
# -*- coding: utf-8 -*-


numitems, capacity = [int(i) for i in input().split()]
data = []

if capacity == 0:
    print(0)
    quit()
    
for _ in range(numitems):
    itemvalue, itemweight = [int(i) for i in input().split()]
    if itemvalue == 0:
        continue
    data.append((itemvalue, itemweight))
    
data.sort(key = lambda x: x[0]/x[1], reverse = True)

total_amt = 0

for itemvalue, itemweight in data:
    if capacity == 0:
        print(total_amt)
        quit()
    amount = min(itemweight, capacity)
    total_amt += amount*itemvalue/itemweight
    capacity -= amount

print(total_amt)
