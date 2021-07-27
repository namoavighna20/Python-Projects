n=int(input("Enter the value of n for pyramid length:"))
a=0
b=' '
j=1
for x in range(n,-1,-1):
    print((x*b)+(j*str(a)))
    a=a+1
    j=j+1


