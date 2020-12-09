import pickle

name_id={}
try:
    ID=int(input("Enter your id: "))
except ValueError:
    print("Please Enter a correct ID")
    ID=int(input("Enter your id: "))


while ID!=999:
    if 1111111<=ID<=9999999:
        options=input("Are you a New User? (Y/N): ")
        
        if options=="Y" or options=="y":
            name=input("Name:")
            
            try:
                with open("testing.txt","wb+")as base:
                    name_id = pickle.load(base)
                    pickle.dump(name_id,base)
            except EOFError:
                name_id[ID]="{}".format(name)
                with open("testing.txt","wb+")as base:
                    pickle.dump(name_id,base)
    
            read_name = open("testing.txt","rb")
            name_id = pickle.load(read_name)
            
           
            
        elif options=="N" or options=="n":
        
            try:
                read_name = open("testing.txt","rb")
                name_id = pickle.load(read_name)
                print(name_id[ID])
            
            except KeyError :     # error checking
                print("You are a new user!!")
                continue
            except EOFError:     # error checking
                print("You are a new user!!")
                continue
            except FileNotFoundError :     # error checking
                print("You are a new user!!")
                continue            

        else:
            print("You have entered a wrong options")
    else:
        print("Please enter a correct ID")
        print("Example: 1234567")


    try:
        ID=int(input("Enter your id: "))
    except ValueError:
        print("Please Enter a correct ID")
        ID=int(input("Enter your id: "))

#Menu
read_name = open("testing.txt","rb")
name_id = pickle.load(read_name)
count=1
for elements in name_id:
    print("{} . {} ----- {}".format(count,elements,name_id[elements]))
    count+=1
