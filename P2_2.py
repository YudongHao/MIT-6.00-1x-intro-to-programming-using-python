#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:29:07 2016

@author: yudonghao
"""

def minimumdebt(balance, AIR):
    '''
    AIR = annualinterestrate
    MPR = monthlypaymentrate
    '''
    LP = 10
    b = balance
    while b > 0:
        b = balance
        LP += 10
        for i in range(0, 12):
            ub = b - LP
            b = ub*(1+AIR/12)
    return LP

print minimumdebt(3329, 0.2)