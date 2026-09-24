x=input()
f1=[]
f=x.split()
for i in f:
    a=int(i)
    
    f1+=[a]

f2=sum(f1)   
f3=len(f1)
g=[]
m=f2/f3
for i in f:
    a=int(i)
    a1=m-a
    b=abs(a1)
    g+=[b]

g1=sum(g)

if float(g1)==int(g1):
    print(int(g1))
else:
    print(float(g1))


