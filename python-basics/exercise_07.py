x=str(input())


a=x.find("AB")
if a!=(-1):
    c=a+2
    b=x.find("BA",c)
    if b!=(-1):
        print("YES")


a=x.find("BA")
if a!=(-1):
    c=a+2
    b=x.find("AB",c)
    if b!=(-1):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
