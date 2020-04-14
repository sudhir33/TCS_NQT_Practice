def valid(st):
    s=0
    l=[0 for i in st]
    ind=0
    for i in st:
        c=st.count(i)
        l[ind]=c
        ind=ind+1
    one=0
    for i in l:
        if i==1:
            one+=1
        if one==2:
            return "Not valid"
    if one==1:
        return "make it valid"
    return "valid"
        
st=input()
res=valid(st)
print(res)
