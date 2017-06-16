# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def deep_reverse(Eco): 
    if len(Eco)==1 and type(Eco[0])== list:
        return deep_reverse(Eco[0])
    else:
        for i in range(int((len(Eco)+1)/2)):
            if type(Eco[i]) == list and type(Eco[(len(Eco)-1-i)]) == list:
                if i!= len(Eco)-1-i:
                    Eco[i] = deep_reverse(Eco[i])
                    Eco[(len(Eco)-1-i)] = deep_reverse(Eco[(len(Eco)-1-i)])
                else:
                    Eco[i] = deep_reverse(Eco[i])
                temp = Eco[i]
                Eco[i]= Eco[(len(Eco)-1-i)]
                Eco[(len(Eco)-1-i)] = temp
            else:
                temp = Eco[i]
                Eco[i]= Eco[(len(Eco)-1-i)]
                Eco[(len(Eco)-1-i)] = temp
    return Eco
    
print (deep_reverse([[1500, 1501, -1000, 0, 2000], [1500, 1501, -1000, 0, 2000]]))