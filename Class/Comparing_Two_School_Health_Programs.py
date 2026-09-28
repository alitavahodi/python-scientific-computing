import csv
from statistics import mean
l=["A","B"]
ll=["sen","ghad","vazn"]
class school:
    count=0
    def __init__(self,namecelas,students):
        self.namecelas=namecelas
        self.students=students
        school.count+=1
    def get_names(self):
        return ("celase %s" %self.namecelas)

    def get_students(self):
        return ("celase %s, %i danesh amooz darad" %(self.namecelas,self.students))

    def tedade_celasha(self):
        return ('I have %i classes' %school.count)


class celas(school):
    def miangin(self):
        l=["A","B"]
        compare_list=list()
        for letter in l:
            with open("E:\\Python project\\advanced python jadi\\tamrin1\\%s.csv" %(letter), "r") as f:
                reader=csv.reader(f)
                
                
                for row in reader:
                    w=list()
                    for i in row:
                        w.append(float(i))
                    compare_list.append(float(mean(w)))
                    print(float(mean(w)))
        #print(compare_list)
        f.close()
        if compare_list[1]>compare_list[-2]:
            return "A"
        elif compare_list[1]==compare_list[-2]:
            if compare_list[2]<compare_list[-1]:
                return "A"
            elif compare_list[2]==compare_list[-1]:
                return 'Same'
            else:
                return 'B'
        else:
            return "B"


for letter in l:
    a=int(input("tedade danesh amoozane kelase %s ra vared konid " %letter))

    with open("E:\\Python project\\advanced python jadi\\tamrin1\\%s.csv" %letter,"w",newline="") as x:
        writer=csv.writer(x)
        

        for ii in ll:
            detail=input("%s danesh amoozan ra vared konid " %ii)
            b=detail.split()
            bb=[]
            for iii in b:
                bb.append(float(iii))     #to save float as a list member

            writer.writerow(bb)
    x.close()
    qqq=str(a)   #bcz we want to define a class and the name of it should be a variable not a "str" or "int"
    qqq=school('%s' %letter,a)
    #print(qqq.get_names())
    #print(qqq.get_students())
#print(qqq.tedade_celasha())
print(celas.miangin(5))           



    



    
        




    