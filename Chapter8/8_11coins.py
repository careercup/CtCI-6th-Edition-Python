#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION: calculate the way to representing n cents
#recursive solution
def ccombination(ray,n):
    if n == 0: return 1
    if n < 0: return 0
    if len(ray) == 0: return 0
    m = len(ray)
    return ccombination(ray[:m-1],n) + ccombination(ray,n-ray[m-1])

#Dynamic solution by Afzal Ansari
def count(ray, n):
    table = [0 for k in range(n+1)]
    #first case 0 value
    table[0] = 1
    for i in range(0,len(ray)):
        for j in range(ray[i],n+1):
            table[j] += table[j-ray[i]]
    return table[n]

arr = [1, 5, 10,20,25]
n = 100
print(ccombination(arr, n))
print(count(arr, n))
