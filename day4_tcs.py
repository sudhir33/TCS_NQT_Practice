"""
Day4
String Reverse
16/apr/2020
"""
def reverse(st):
    s=[]
    str1=""
    for i in st: #this is sudhir
        if i==' ':
            s.append(str1)#this is sudhir
            str1=""
        else:
            str1+=i#
    s.append(str1)
    c=0
    for i in s[::-1]:
        if c==0:
            print(i.title(),end=" ")
            c=1
        else:
            print(i,end=" ")
    print()




def rev(st):
    l=st.split()
    return ' '.join(l[::-1])
    
t=int(input())#3 cases
for _ in range(t):
    st=input()
    res=rev(st)
    print(res)






"""
2

there is tcs class

Class tcs is there
"""













