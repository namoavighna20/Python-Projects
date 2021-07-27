print(' ' 'Which operation u want to perform\n'
            '1->Addition\n'
            '2->Substraction\n'
            '3->Multiplication\n'
            '4->Divison'
            ' ' '')
sum=0
subs=0
mulp=1
divs=1
a=int(input("How many numbers you want to enter:"))
b=int(input("Which operation u want to perform:"))
for x in range(1,a+1):
    x=int(input("Enter the number:"))
    if(b==1):
        sum=sum+x
        print("Sum is:",sum)
    elif(b==2):
        subs=x-subs
        print("Substraction is:",subs)
    elif(b==3):
        mulp=mulp*x
        print("Multiplication is:",mulp)
    elif(b==4):
        divs=x/divs
        print("Divison is:",divs)


