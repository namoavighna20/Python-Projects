s=int(input("Enter the number:"))
a=0
b=1
if s<0:
    print("Invalid output")
elif s==0:
    b=a
else:
    for x in range(2,s+1):
        c=a+b
        a=b
        b=c
        print(b)
