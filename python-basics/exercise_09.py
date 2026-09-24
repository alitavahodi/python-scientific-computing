n=input()
item=input().split()
list=[]

for i in item:
    a=int(i)
    if a<=2:
        list+=[a]


b=len(list)
c=int(b/3)
print(c)