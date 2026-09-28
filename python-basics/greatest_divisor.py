def tedade_maghsoom_alaih(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count=count+1
    return count
print("5 adad ra vared konid")
x=5
list=[]
for i in range(x):
    y=int(input())
    list+=[y]

list_2=[]
for i in list:
    a=tedade_maghsoom_alaih(i)
    list_2+=[a]
    b=max(list_2)
    if a==b:
        c=i

print("adadi ke bistarin maghsum alai ra darad= ",c,"           tedad maghsoom alaih haye an= ",b)   

