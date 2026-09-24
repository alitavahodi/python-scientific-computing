x=str(input())
f=str(x.replace("+",""))


g=[]
gg=[]
ggg=[]

for letter in f:
    if letter=="1":
        g+=letter
    elif letter=="2":
        gg+=letter
    elif letter=="3":
        ggg+=letter

f=g+gg+ggg
q='+'.join(f)
print(q)
