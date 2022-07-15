import json
info={}
while True:
    print("\033[34m ","""press\n 1.for create\n 2.for read \n 3.for update \n 4.for delet \n 5.for exist""","\033[0m")
    n=int(input('Enter what do you want to do:'))
    def create():
        try:
            with open("akash.json","r") as p:
                d=json.load(p)
                n=input('Enter your email:')
                if "@" in n:
                    if n not in d:
                        with open("akash.json","w") as p1:
                            j={"name":input("Enter the name:"),"Roll no":int(input("Enter the Roll no:")),"percent":int(input('enter the percentage:'))}
                            d[n]=j
                            json.dump(d,p1,indent=4)
                            print("your creating account sucessful.")
                    else:
                        print("\033[31m ","This Email already exist","\033[0m")
                else:
                    print("\033[33m ","please enter correct Email.","\033[0m")
        except:
            n=input("Enter your Email:")
            if "@" in n:
                with open("akash.json","w") as m:
                    j={"name":input('Enter your Name:'),"Roll no":int(input("Enter your Roll No:")),"percent":int(input('enter the percentage:'))}
                    info[n]=j
                    json.dump(info,m,indent=4)
                    print("your creating account sucessful.")
            else:
                print("\033[32m ","please enter your correct Email","\033[0m")
    def read():
        try:
            n=input("Enter your Email:")
            with open("akash.json","r") as p:
                d=json.load(p)
                if n in d:
                    print(d[n])
                else:
                    print("\033[31m ","This Email does not exist in this file.","\033[0m")
        except:
                print("\033[33m","Please create file before read.","\033[0m")
    def update():
        try:   
            n=input("Enter your Email:")
            with open("akash.json","r") as p:
                d=json.load(p)
            if n in d:
                with open("akash.json","w") as p1:
                    j={"name":input("Enter your Name:"),"Roll no":int(input("Enter your Roll no:")),"percent":int(input('enter the percentage:'))}
                    d[n]=j
                    json.dump(d,p1,indent=4)
                    print("your updating sucessful.")
            else:
               print("\033[31m ","This Email does not exist in this file.","\033[0m")
        except:
            print("\033[33m","you have no any file to update.","\033[0m")
    def delet():
        try:
            n=input("Enter your Email:")
            with open("akash.json","r") as p2:
                d=json.load(p2)
            if n in d:
                with open("akash.json","w") as p3:
                    d.pop(n)
                    json.dump(d,p3,indent=4)
                    print("your deleting sucessful.")
            else:
                print("\033[31m ","This Email does not exist.","\033[0m")
        except:
            print("\033[33m","you have no any file info to delet.","\033[0m")

    if n==1:
        create()
    elif n==2:
        read()
    elif n==3:
        update()
    elif n==4:
        delet()
    elif n==5:
        break
