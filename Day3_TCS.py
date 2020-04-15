"""
Binary to Octal conversion
15/apr/2020
TCS NQT DAY3 Solution
"""
def bi_to_oct(n):
    l=list(n)
    size=len(l)
    c=0
    res=""
    r=0
    for i in range(size-1,-1,-1):
        if l[i]=='1':
            r=r+(2**c)
        c=c+1
        if c==3 or i==0:
            c=0
            res=str(r)+res
            r=0
    #print(res)
    return res

n=input()
res=bi_to_oct(n)
print(res)
