#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:00:51 2016

@author: yudonghao
"""

def minimumdebt(balance, AIR, MPR):
    '''
    AIR = annualinterestrate
    MPR = monthlypaymentrate
    '''
    r = AIR/12
    b = balance
    for i in range(0, 12):
        ub = b*(1-MPR)
        b = ub*(1+r)
    return round(b, 2)
print minimumdebt(484, 0.2, 0.04)