#patients list
from cmath import pi
from curses.ascii import isdigit
from curses.panel import new_panel
from hashlib import new
from os import extsep, initgroups
from re import I
from this import d

#global 
#to store record patients
new_patients=[]
#to store record nurses
new_nurses=[]
#to store record assigned pateints to the nurses
new_assignment={}
def name_strip(name):
    new_nme=''
    name=name.strip()
    cntr=0
    for i in name:
        if i == " " and name[cntr-1] == " ":
            new_nme=new_nme
        else:
            new_nme+=i
        cntr+=1
    return new_nme

def newadd(type):
    print(type)
    if type == "patient":
        print("add pateint::")
        if len(new_patients) == 0:
            pid=1
            name=input("enter the name of patient")
            if name.replace(" ", "").isalpha() == False:
                print("Invalid Input")
            else:
                name=name.lower()
                name=name_strip(name)
                new_patients.append({'id':pid,'name':name})
        else:
            pid=0
            for item in new_patients:
                pid=item["id"]
            pid+=1
            print(pid)
            name=input("enter the name of patient")
            if name.replace(" ", "").isalpha() == False:
                print("Invalid Input")
            else:
                name=name.lower()
                name=name_strip(name)
                new_patients.append({'id':pid,'name':name})
        print(new_patients)
    elif type == "nurse":
        print("add nurse::")
        if len(new_nurses) == 0:
            nid=1
            name=input("enter the name of nurse")
            if name.replace(" ", "").isalpha() == False:
                print("Invalid Input")
            else:
                name=name.lower()
                name=name_strip(name)
                new_nurses.append({'id':nid,'name':name})
        else:
            nid=0
            for item in new_nurses:
                nid=item["id"]
            nid=nid+1
            print(nid)
            name=input("enter the name of nurse")
            if name.replace(" ", "").isalpha() == False:
                print("Invalid Input")
            else:
                name=name.lower()
                name=name_strip(name)
                new_nurses.append({'id':nid,'name':name})
        print(new_nurses)
def newassign():
    typep="patient"
    typen="nurse"
    valp=list(typep)
    valn=list(typen)
    if valp != 0 and valn != 0:
        n_id=input("enter the id of nurse")
        p_id=input("enter the id of patient")
        if n_id.isdigit() == False:
            print("invalid nurse id")
        elif p_id.isdigit() == False:
            print("invalid patient id")
        else:
            n_id=int(n_id)
            p_id=int(p_id)
            n_exst=0
            p_exst=0
            for item in new_patients:
                if p_id == item["id"]:
                    p_exst=1
                    break
            for item in new_nurses:
                if n_id == item["id"]:
                    n_exst=1
                    break
            if p_exst == 1 and n_exst == 1:
                if len(new_assignment) == 0 :
                    new_pat=[]
                    new_pat.append(p_id)
                    new_assignment[n_id]=new_pat
                else:
                    p_check=any(p_id in val for val in new_assignment.values())
                    if p_check == True:
                        print("pateint already assgined")
                    else:
                        if n_id in new_assignment:
                            if len(new_assignment[n_id]) >= 2:
                                print("nurse have already 2 pateints assigned")
                            else:
                                new_assignment[n_id].append(p_id)
                        else:
                            new_pat=[]
                            new_pat.append(p_id)
                            #index = mylist.index(item)
                            new_assignment[n_id]=new_pat
            elif p_exst != 1:
                print("no patient")
            elif n_exst != 1:
                print("no nurse")
def newdelete(type):
    if type == "patient":
        p_exst=0
        print("delete pateint")
        val=list(type)
        if val == 0:
            print(" ")
        else:
            d_id=input("enter the ID of patient")
            if d_id.isdigit() == False:
                print("invalid id")
            else:
                d_id=int(d_id)
                for item in new_patients.copy():
                    if d_id == item["id"]:
                        new_patients.remove(item)
                        p_exst=1
                        break
                if p_exst == 1:
                    print(new_assignment.values())
                    for i in new_assignment.values():
                        if d_id in i:
                            i.remove(d_id)
                    print(new_assignment)
                else:
                    print("no patient exist")
    elif type == "nurse":
        print("delete nurse")
        val=list(type)
        if val == 0:
            print(" ")
        else:
            p_exst=0
            d_id=input("enter the ID of nurse")
            if d_id.isdigit() == False:
                print("invalid id")
            else:
                d_id=int(d_id)
                for item in new_nurses.copy():
                    if item["id"] == d_id:
                        new_nurses.remove(item)
                        p_exst=1
                        break
                    else:
                        p_exst=0
                if p_exst == 1:
                    
                    if d_id in new_assignment:
                        del new_assignment[d_id]
                else:
                    print("no nurse exist")
def newedit(type):
    if type == "patient":
        print("edit pateint")
        val=list(type)
        if val == 0:
            print(" ")
        else:
            p_exst=0
            e_id=input("Enter the patient ID to be Edited")
            if e_id.isdigit() == False:
                print("invalid id")
            else:
                e_id=int(e_id)
                for item in new_patients.copy():
                    if item["id"] == e_id:
                        e_name=input("enter new name")
                        if e_name.replace(" ", "").isalpha() == False:
                            print("Invalid Input")
                        else:
                            e_name=e_name.lower()
                            e_name=name_strip(e_name)
                            item["name"]=e_name
                            p_exst=1
                            break
                    else:
                        print("no patient exist")
    elif type == "nurse":
        print("edit nurse")
        val=list(type)
        if val == 0:
            print(" ")
        else:
            p_exst=0
            e_id=input("Enter the Nurse ID to be Edited")
            if e_id.isdigit() == False:
                print("invalid id")
            else:
                e_id=int(e_id)
                for item in new_nurses.copy():
                    if item["id"] == e_id:
                        e_name=input("enter new name")
                        if e_name.replace(" ", "").isalpha() == False:
                            print("Invalid Input")
                        else:
                            e_name=e_name.lower()
                            e_name=name_strip(e_name)
                            item["name"]=e_name
                            p_exst=1
                            break
                    else:
                        print("no nurse exist")         

print("##########################")
print(" Nurse Management System")
print("##########################")
print("WELCOME!")
nchoice="n"
while nchoice == "n":
    print(" ")
    print(" ")
    print("1=Patients \n2=Nurses \n3=Assign Patients to the nurses \n4=view assign nurses \n5=Exit")
    print(" ")
    choice= input("Enter choice:")
    print(choice)
    if choice.isdigit() == False:
        print("invalid input")
    else:
        choice=int(choice)
    if choice == 1:
        pnchoice="n"
        while pnchoice == "n":
            print(" ")
            print(" ")
            print("1=Add patient \n2=Delete patient \n3=list patient \n4=edit patient \n5=exit")
            print(" ")
            pchoice=input("enter option")
            if pchoice.isdigit() == False:
                print("invalid input")
            else:
                pchoice=int(pchoice)
                type="patient"
                if pchoice == 1:
                    newadd(type)
                elif pchoice ==2:
                    newdelete(type)
                elif pchoice == 3:
                    list(type)
                elif pchoice == 4:
                    newedit(type)
                elif pchoice == 5:
                    break
                else:
                    print("invalid option")
    elif choice == 2:
        nnchoice="n"
        while nnchoice == "n":
            print(" ")
            print(" ")
            print("1=Add nurse \n2=Delete nurse \n3=list nurse \n4=edit nurse \n5=exit")
            pchoice=input("enter option")
            if pchoice.isdigit() == False:
                print("invalid input")
            else:
                pchoice=int(pchoice)
                type="nurse"
                if pchoice == 1:
                    newadd(type)
                elif pchoice ==2:
                    newdelete(type)
                elif pchoice == 3:
                    list(type)
                elif pchoice == 4:
                    newedit(type)
                elif pchoice == 5:
                    break
                else:
                    print("invalid option")
    elif choice == 3:
        print(" ")
        print(" ")
        newassign()
    elif choice == 4:
        print(" ")
        print(" ")
        # for key, value in assignment.items():
        #     print("Pid => Nid")
        #     print(str(value) + " => " + str(key))
        for key, value in new_assignment.items():
            print("Pid => Nid")
            print(str(value) + " => " + str(key))
    elif choice == 5:
        nchoice="y"
    else:  
        print(" ")
        print(" ")  
        print("invalid choice")
    