#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#inputs




def merging(left, right):
    k, j, inv = 0,0,0
    fin = list()
    
    while k < len(left) and j < len(right):
        if left[k] <= right[j]:
            fin.append(left[k])
            k += 1
        else:
            fin.append(right[j])
            inv += len(left) - k
            j += 1
    
    fin += left[k:]
    fin += right[j:]
    return fin, inv

def sorting(mat):
    global total
    if len(mat) <= 1:
        return mat
    midpt = len(mat)//2
    
    left = sorting(mat[:midpt])
    right = sorting(mat[midpt:])
    
    sortmat, fill = merging(left,right)
    total += fill
    
    return sortmat

total = 0
num = int(input())
sequence = [int(i) for i in input().split()]
sorting(sequence)
print(total)


    
    