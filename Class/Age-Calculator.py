import datetime
class know_your_age:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    def senamo_begoo(self):
        tooday=datetime.datetime.today()
        #now_day=tooday.day
        #now_month=tooday.month
        now_year=tooday.year

        if self.month>12:
            print('Wrong')
            return
        if self.day>31:
            print("wrong")
            return

        
        #age_day=(now_day)-(self.day)
        #age_month=(now_month)-(self.month)
        age_year=(now_year)-(self.year)
        print("sene shoma %i sal ast" %(age_year))



b=input('sene miladie khod ra ba tartib "sal/mah/rooz" vared konid  ')
a=b.split("/")
c=list()
for i in a:
    c.append(int(i))


age=know_your_age(c[0],c[1],c[2])
age.senamo_begoo()
 


