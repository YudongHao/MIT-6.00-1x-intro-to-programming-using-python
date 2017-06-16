#!/usr/bin/env python2
# -*- coding: utf-8 -*-n
"""
Created on Fri Nov  4 13:04:44 2016

@author: yudonghao
"""

def minimumdebt(balance, AIR):
    '''
    AIR = annualinterestrate
    '''
    b =balance
    LP = low = b/12.0
    high = b*((1+AIR/12.0)**12)/12.0
    u = 0.01
    while abs(b - LP) > u:
        if b > LP:
            low = LP 
        else:
            high = LP
        LP = (low + high)/2.0
        b = balance
        for i in range(0, 11):
            ub = b - LP
            b = ub*(1+AIR/12.0)
    return round(LP, 2)

print minimumdebt(999999, 0.18)