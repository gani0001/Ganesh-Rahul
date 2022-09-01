lower= int(input("enter the lower"))
upper = int(input("enter the upper"))
prime = []
composite = []

for i in range(lower,upper):
        for p in range(2, i):
            if (i % p)==0:
                composite.append(i)
                break
        else:
            prime.append(i)
print("prime: ",prime)
print("composite: ",composite)


