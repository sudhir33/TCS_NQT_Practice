#Python code
def fun(st):
    l=list(st)#t h i s _ i s _ s u d h i r _ _ _ _ _
    l.reverse()
    sp=0
    for i in l:#last spaces count
        if i!='_':
            break
        sp=sp+1#5

    l.reverse()
    l=l[:len(l)-sp]#t h i s _ _ _ _ i s _ _ _ s u d h i r #sp=1
    i=0 
    s=1#+1
    k=2# imp value
    while s<=sp:
        if l[i]=="_":
            l.insert(i+1,"_")
            i=i+k
            s=s+1
        else:
            i=i+1
        if i==len(l)-1:#return back to first char
            i=0
            k=k+1        
    s=''.join(l)
    return s











#this___is___tcs__session

st=input()
res=fun(st)
print(res)


