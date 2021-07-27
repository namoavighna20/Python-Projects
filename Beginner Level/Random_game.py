import random
a=random.randint(1,100)
print(a)
while(1):
    n=int(input("Enter the number:"))
    if(n>=a+5):
        print("Your guess is too large.Try Again!")
    elif(0<=n<=a-5):
        print("Your guess is too small.Try Again!")
    elif(n==a):
        print("Congratulations!You Won")
        break
    elif(n<0):
        print("You Quit")
        break
    else:
        print("You are closer to your guess")