import csv
from csv import writer
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):    
    with open("E:\\Python project\\tamrin13\\%s.csv" %(input_file_name), "r") as f:
        reader=csv.reader(f)
        with open("E:\\Python project\\tamrin13\\%s.csv" %(output_file_name),"w",newline="") as x:
            writer=csv.writer(x)

            for row in reader:
                n=row[0].strip()
                grades=list()
                for i in row[1:]:
                    grades.append(int(i.strip()))
                l=[n,mean(grades)]   

                writer.writerow(l)
    
#calculate_averages("tamrin 13","a")

def calculate_sorted_averages(input_file_name, output_file_name):
        with open("E:\\Python project\\tamrin13\\%s.csv" %(input_file_name), "r") as f:
            reader=csv.reader(f)
            with open("E:\\Python project\\tamrin13\\%s.csv" %(output_file_name),"w",newline="") as x:
                writer=csv.writer(x)

                d=dict()
                for row in reader:
                    name=row[0]
                    v=float(row[1])
                    d[name]=v
                    a=sorted(d.values())
                    b=d.keys()
                    l=list()
                    for i in a:
                        for ii in b:
                            if d[ii]==i:
                                l.append(ii)
                                l.append(i)
                
               
                for i in range(int(len(l)/2)): #len/2 baraye ine ke range az tedad ozve list bishtar nashe err bede
                    ll=list()
                    n=2*i
                    m=2*i+1
                    ll.append(l[n])
                    ll.append(l[m])

                    writer.writerow(ll)

calculate_sorted_averages("a","b")    
                                
def calculate_three_best(input_file_name, output_file_name):
    with open("E:\\Python project\\tamrin13\\%s.csv" %(input_file_name), "r") as f:
            reader=csv.reader(f)
            with open("E:\\Python project\\tamrin13\\%s.csv" %(output_file_name),"w",newline="") as x:
                writer=csv.writer(x)

                d=dict()
                for row in reader:
                    name=row[0]
                    m=float(row[1])
                    d[name]=m
                    a=sorted(d.values())
                    b=d.keys()

                aa=list()
                aa=[a[-1],a[-2],a[-3]]      #soarted 3 best 
                
                l=list()
                for i in aa:
                    for ii in b:
                        if d[ii]==i:
                            l.append(ii)
                            l.append(i)

                for i in range(int(len(l)/2)):
                    ll=list()
                    n=2*i
                    m=2*i+1
                    ll.append(l[n])
                    ll.append(l[m])

                    writer.writerow(ll)

#calculate_three_best("b","c") 
                                                                             
def calculate_three_worst(input_file_name, output_file_name):
    with open("E:\\Python project\\tamrin13\\%s.csv" %(input_file_name), "r") as f:
            reader=csv.reader(f)
            with open("E:\\Python project\\tamrin13\\%s.csv" %(output_file_name),"w",newline="") as x:
                writer=csv.writer(x)

                d=dict()
                for row in reader:
                    name=row[0]
                    m=float(row[1])
                    d[name]=m
                    a=sorted(d.values())

                aa=list()
                aa+=[a[0],a[1],a[2]]

                for i in range(len(aa)):
                    ll=[]
                    ll.append(aa[i])

                    writer.writerow(ll)

#calculate_three_worst("b","d") 
                       
def calculate_average_of_averages(input_file_name, output_file_name):
    with open("E:\\Python project\\tamrin13\\%s.csv" %(input_file_name), "r") as f:
            reader=csv.reader(f)
            with open("E:\\Python project\\tamrin13\\%s.csv" %(output_file_name),"w",newline="") as x:
                writer=csv.writer(x)

                l=[]
                for row in reader:
                    m=float(row[1])
                    l+=[m]
                ll=[mean(l)]

                writer.writerow(ll)
                         
#calculate_average_of_averages("b","e")