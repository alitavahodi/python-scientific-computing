from collections import OrderedDict

n=int(input())
q=[]

for i in range(n):
    a=input()
    q+=[a]

q.sort()
f=OrderedDict()

for letter in q:
    f[letter]=f.get(letter,0)+1

for i in list(f.keys()):
    print(i,f[i])
    

  