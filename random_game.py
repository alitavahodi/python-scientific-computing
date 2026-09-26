print("keep your number in mind between 1-100")

import random
x=1
y=99
a=random.randint(x,y)
print("my guess is ",a)

answer=input()

while answer!="d":
    if answer=="b":
        x=a
    elif answer=="k":
        y=a
    a=random.randint(x,y)
    print("what about ",a," ?")
    answer=input()


        
print("ohhh yesssss baby!")
