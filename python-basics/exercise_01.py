x=str(input())
x=x.lower()
horuf=int(len(x))

f=[]


for letter in x:
    if letter=="a":
        y=x.find(letter)
        a=y+1
        x=x[:y]+x[a:]
    elif letter=="o":
        y=x.find(letter)
        a=y+1
        x=x[:y]+x[a:]
    elif letter=="i":
        y=x.find(letter)
        a=y+1
        x=x[:y]+x[a:]
    elif letter=="u":
        y=x.find(letter)
        a=y+1
        x=x[:y]+x[a:]
    elif letter=="e":
        y=x.find(letter)
        a=y+1
        x=x[:y]+x[a:]

for letter in x:
    f+=letter
    
x=".".join(f)   
x="."+x[:horuf]
print(x)

