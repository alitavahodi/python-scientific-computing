import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    with open("E:\\Python project\\tamrin14\\%s.csv" %(input_file_name), "r") as f:
        reader=csv.reader(f)
        with open("E:\\Python project\\tamrin14\\%s.csv" %(output_file_name),"w",newline="") as x:
            writer=csv.writer(x)

            dict={}
            for i in range(1000,10000):
                a=hashlib.sha256(b"%i" %(i)).hexdigest()
                dict[a]=i

            for row in reader:
                name=row[0]
                name_code=row[1]
                b=dict[name_code]

                writer.writerow([name,b])
            
hash_password_hack("a","b")

