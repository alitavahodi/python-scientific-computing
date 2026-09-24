x=str(input())
a=0
b=0


for letter in x:
    if letter==letter.upper():
        a=a+1
    else:
        b=b+1
if a>b:
    print(x.upper())
else:
    print(x.lower())
