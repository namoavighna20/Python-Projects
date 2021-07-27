while(1):
    s=input("Enter the Word:")
    a=len(s)
    b=s[-1:-a-1:-1]
    print(b)
    if(b==s):
        print("Word is Pallindrome")
    else:
        print("Word is not pallindrome")
