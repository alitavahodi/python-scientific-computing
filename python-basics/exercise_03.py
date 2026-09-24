x=[str(input())]
y=[]
w=[]

for i in range(1,10):
    x+=[str(input())]

for i in x:
    z=i.lower()
    y+=[z]

for i in y:
    a=i[0].upper()
    b=a+i[1:]
    w+=[b]
for i in w:
    print(i)
 

