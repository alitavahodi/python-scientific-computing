x=[int(input("sen? "))]

while True:
    y=int(input())
    if y==-1:
        break
    x+=[y]
a=max(x)
print(a)
x.remove(a)
print(max(x))

