x=str(input())

a=x.find("A")
if a==-1:
    print("NO")
else:
    b=a+1
    c=x[b]
    if c=="B":
        d=b+1
        e=x.find("B",d)
        if e==-1:
            print("NO")
        else:
            f=d+1
            g=x[f]
            if g=="A":
                print("YES")
            else:
                print("NO")
    else:
        print("NO")    

            


