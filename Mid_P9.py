#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:59:11 2016

@author: yudonghao
"""

def flatten_helper(aList,flat):
    for i in aList:
        if type(i) == list:
            flatten_helper(i, flat)
        else:
            flat.append(i)      

def flatten(aList):
    flat = []
    flatten_helper(aList,flat)
    return flat
    
print(flatten([[1]]))