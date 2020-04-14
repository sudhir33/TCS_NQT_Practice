def value(r): 
    if (r == 'I'): 
        return 1
    if (r == 'V'): 
        return 5
    if (r == 'X'): 
        return 10
    if (r == 'L'): 
        return 50
    if (r == 'C'): 
        return 100
    if (r == 'D'): 
        return 500
    if (r == 'M'): 
        return 1000
    return -1


def romanToDecimal(s):#MCMIV
    res=0
    i=0
    while(i<len(s)):
        s1=value(s[i])#100
        if (i+1 <len(s)):#LAST VAL
            s2=value(s[i+1])#1000
            if s1>=s2:#100>=1000
                res=res+s1#
                i=i+1#
            else:
                res=res+(s2-s1)#1000+900
                i=i+2#2
        else:
            res=res+s1
            i=i+1
    return res








"""
input: M C M I V

"""

s=input()
res=romanToDecimal(s)#MCMIV
print(res) 





