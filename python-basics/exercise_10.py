
n=int(input())
f=[]
g=[]

for i in range(n):

    x=input().split()
    a=int(x[0])
    b=int(x[1])
    
    del x[0]
    del x[0]
    
    x+=[a,b]      #برای اینکه رشته نباشه اعضا عدد باشه
    f+=[x]        #مجموعه ای شد که اعضاش مجموعه هایی اند با اعضای کیفیت و قیمت لپتاپ
    
for i in f:
    a=i
    b=a[1]
    c=a[0]
    for i in f:
        x=i
        d=x[1]
        e=x[0]
        if d>b and e<c:
            g+=["happy irsa"]
            break
        elif d==b and e<c:
            g+=['happy irsa']
            break
if len(g)>0:
    print('happy irsa')
else:
    print("poor irsa")
        
            
            
    


    


    

        

   
        



    