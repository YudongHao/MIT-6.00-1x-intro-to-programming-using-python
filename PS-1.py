# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s = 'tusoqcwsgww'
res = []
alpha = []
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        alpha.append(s[i])
    else:
        alpha.append(s[i])
        res.append(alpha)
        alpha = []
if s[-2] <= s[-1]:
    alpha.append(s[-1])
    res.append(alpha)
print res
longest = ""
same = []
for i in range(len(res)):
    if len(longest) < len(res[i]):
        longest = res[i]
final = "".join(longest)
print final
