
import random
class human:
    count=0
    all=list()
    def __init__(self,name,number):
        self.name=name
        self.number=number
        human.count+=1
        self.all.append(self.name)
    

      
class football_player(human):
     def retun_all(self):
          return human.all
    



a=input('esme bazikonan ra vared konid  ')
b=a.split('-')

#print(b)
d=list()
for i in range(1,99):    #shomare pirhane bazikona
    if len(d)<22:       #22 ta bazinon darim
        d.append(i)

#print(d)  
for i in b:        #add players as an object
        n=d.pop()
        qq=football_player(i,n)

X=qq.retun_all()
#print(len(X))
#print(qq.retun_all())
#print(human.count)

TEAM_A=[]

for i in range(1,12):
    qwe=random.choice(X)
    TEAM_A.append(qwe)
    X.remove(qwe)

print('TEAM_A= ',TEAM_A)
print(len(TEAM_A))         

TEAM_B=X
#print(len(qq.retun_all))
print("TEAM B= ",TEAM_B)
print(len(TEAM_B))



    




    
    
