from time import sleep
import datetime
import os

def create_password():
    print("\n---------------------------------------------------------------\n")
    print("\n--------------------  Create New Password  --------------------\n")
    while(1):
        n=input("\n\nEnter the Password: ")
        m=input("\nConfirm The Password: ")
        if(n==m):
            f=open("pass.txt","w")
            f.write(""+m+"")
            f.close()
            break
        else: print("\n\nPassword Didn't Match Try Again")
    print("\n---------------------- Password Created -----------------------\n\n")

def password_check(string):
    f=open("pass.txt","r")
    st=[]
    for l in f:
        st.append(l)
    ne="".join(st)
    f.close()
    if(ne==string): return 1
    else: return 0
    
f=open("pass.txt","a")
f.close()

print("\n\n---------------------------------------------------------------\n")
print("-----------------  Library Management System  -----------------\n\n")

if (os.path.getsize('pass.txt') == 0):
    print("\n\n - Password is Not Set -\n - Set a Strong Password For Your System -\n - Remember Your Password - \n - Password Can be Set Once Only\n\n")
    create_password()
print("\n---------------------------------------------------------------\n")
print(" - You Need to Enter Password to Continue")
print(" - You Have only 3 chances to Enter Password")
ti=1
o=25
over=1
while(over):
    string=input("\n - Enter Password: ")
    a=password_check(string)
    if(a):
        print("\n\n---------------------------------------------------------------\n")
        print("\n-------------------  Welcome to the System  -------------------\n\n")
        while(1):
            print("\n\n---------------------------------------------------------------")
            a=int(input("\n1: Add a Book\n2: Delete a Book\n3: Display All Books\n4: Book Borrow Request\n5: Book Return Request\n6: Enter '0' to Exit\n\nEnter Your Choice: "))
            if(a==0):
                print("\n\n------------------------------------------------------\n")
                print("-------------Thanks For Using Our Service-------------\n")
                over=0
                break
            elif(a==1):
                print("\n\n---------------------------------------------------------------\n")
                print("-------------------  Enter the Book's Data  -------------------\n")
                f=open("libdata.txt","a")
                name=input("\n - Enter the Name of the Book: ")
                author=input("\n - Enter the Name of the Author: ")
                book_id=input("\n - Enter the Book ID: ")
                status=input("\n - Status(Avail/Issued): ")
                f.writelines("\n"+name.capitalize()+"  "+author.capitalize()+"  "+book_id+"  "+status.capitalize())
                f.close()
            elif(a==2):
                print("\n\n---------------------------------------------------------------\n")
                print("-------------------  Enter the Book's Data  -------------------\n")
                name=input("\n - Enter Book Name: ")
                found=0
                f=open("libdata.txt","r")
                g=open("new.txt","w")
                data=f.readlines()
                f.close()
                for i in data:
                    j=i.split()
                    if((name.capitalize()) in j):
                        found=1
                        continue
                    else:
                        g.writelines(""+i)
            
                g.close()
                f=open("libdata.txt","w")
                g=open("new.txt","r")
                for i in g:
                    f.write(""+i)
                if(found): print("\n -- Book Deleted -- \n")
                else: print("\n -- Book Not Found -- \n")
            elif(a==3):
                print("\n\n---------------------------------------------------------------\n")
                print("--------------------  All Book's Details  --------------------\n\n")
                f=open("libdata.txt","r")
                print("\n   Name\tAuthor\tBook-Id\tStatus\n")
                data=f.readlines()
                for i in range(1,len(data)):
                    print(i,": ",data[i],end="\n")
                f.close()
                print("\n\n---------------------------------------------------------------\n")
            elif(a==4):
                print("\n\n---------------------------------------------------------------\n")
                print("-------------------  Book Borrow Request  -------------------\n")
                name=input("\n - Enter Book Name: ")
                found=0
                f=open("libdata.txt","r")
                g=open("new.txt","w")
                data=f.readlines()
                f.close()
                for i in data:
                    j=i.split()
                    if((name.capitalize()) in j):
                        found=1
                        j[-1]="Issued"
                        g.writelines(" ".join(j))
                    else:
                        g.writelines(""+i)
                g.close()
                f=open("libdata.txt","w")
                g=open("new.txt","r")
                for i in g:
                    f.write(""+i)
                if(found): print("\n -- Book Updated -- \n")
                else: print("\n -- Book Not Found -- \n")
            elif(a==5):
                print("\n\n---------------------------------------------------------------\n")
                print("-------------------  Book Return Request  -------------------\n")
                name=input("\n - Enter Book Name: ")
                found=0
                f=open("libdata.txt","r")
                g=open("new.txt","w")
                data=f.readlines()
                f.close()
                for i in data:
                    j=i.split()
                    if((name.capitalize()) in j):
                        found=1
                        j[-1]="Avail"
                        g.writelines(" ".join(j))
                    else:
                        g.write(""+i)
                g.close()
                f=open("libdata.txt","w")
                g=open("new.txt","r")
                for i in g:
                    f.write(""+i)
                if(found): print("\n -- Book Updated -- \n")
                else: print("\n -- Book Not Found -- \n")
            else:
                print("\n - Wrong Choice Try Again - \n")
    elif(ti<3):
        print("\n\n---------------------------------------------------------------\n")
        print("\n - Incorrect Password Try Again - \n - You Have only",3-ti,"Attempts -\n\n")
        ti+=1
    elif(o>125):
        print("\n\n---------------------------------------------------------------")
        print("\n - Too Many Attempts - \n - GoodBye - \n\n")
    else:
        print("\n\n---------------------------------------------------------------\n")
        print("\n - You Have Used all 3 Chance's\n - Wait for",o,"Secounds\n")
        ti=1
        sleep(o)
        o+=25
                