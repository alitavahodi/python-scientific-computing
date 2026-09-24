n=int(input())
f=[]
g={}

for i in range(n):
    a=input()
    f=a.split()
    b=f[0]
    c=f[1]
    g[b]=c

q=str(input())
l=q.split()
p=[]

for i in l:
    if i in g:
        b=g[i]
        p+=[b]
    else:
        p+=[i]

print(' '.join(p))




    
    
