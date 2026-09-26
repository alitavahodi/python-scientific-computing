def factoriel(n):
    factor=1
    while n>0:
        factor=factor*n
        n=n-1
        print("while in loop",factor)
    print("out of loop",factor)
    return factor
def f(x):
    return x**3
def Dif1(x):
    h=0.000001
    s=(f(x+h)-f(x))/h
    return s
def Dif2(x):
    h=0.000001
    p=(Dif1(x+h)-Dif1(x))/h
    return p
def Dif3(x):
    h=0.000001
    t=(Dif2(x+h)-Dif2(x))/h
    return t

n=int(input('n='))
print('f(n)=',f(n))
print('Dif1(f(n))=',Dif1(n))
print('Dif2(f(n))=',Dif2(n))
print('Dif3(f(n))=',Dif3(n))

a=float(input('a='))
print('f(a)=',f(a))

part1=f(a)
part2=Dif1(a)*(n-a)
part3=(Dif2(a)*((n-a)**2))/2
part4=(Dif3(a)*((n-a)**3))/6

print("part1=",part1)
print('part2=',part2)
print('part3=',part3)
print('part4=',part4)
taylor=part1+part2+part3+part4
print("taylor=",taylor)


