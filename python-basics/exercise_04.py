a=str(input())
count=0

for letter in a:
    if letter=="h":
        b=a.find(letter)
    elif letter=="e":
        c=a.find(letter)
    elif letter=="l":
        d=a.find(letter)
        count=count+1
    elif letter=="o":
        e=a.find(letter)
if b<c<d<e and count>1:
    print("YES")
else:
    print("NO")

