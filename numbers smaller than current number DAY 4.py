a=int(input("enter the length of the list:"))
(c,e)=([],[])
if(a>0):
    for i in range(0,a):
        b=int(input("enter the element:"))
        c.append(b)
    for i in range(0,a):
        b=0
        for j in range(0,a):
            if(c[j]<c[i]):
                b=b+1
        e.append(b)
    print("input=",c)
    print("output",e)
else:
    print("invalid input")
