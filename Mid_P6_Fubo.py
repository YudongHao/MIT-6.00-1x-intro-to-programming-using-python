#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 21:23:05 2016

@author: yudonghao
"""

L = [[1, 2], 3, 4, 5, 6, 7]

def deep_reverse(x):
    if type(x) != list:
        return
    for i in range(int((len(x)+1)/2)):
        if type(x[i]) == list:
            deep_reverse(x[i])
        if type(x[len(x)-i-1]) == list and i != len(x)-i-1:
            deep_reverse(x[len(x)-i-1])
        #swap
        temp = x[i]
        x[i] = x[len(x)-i-1]
        x[len(x)-i-1] = temp

deep_reverse(L)
print(L)

        
    