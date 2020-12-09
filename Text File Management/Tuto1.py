##stu_list = ["2002222","s"]
##
##with open ("Testing.txt","r+")as f:
##    f_lines = f.readlines()
##    f.seek(0)
##    for line in f_lines:
##        if stu_list[0]!=line.strip("\n").split("|")[0]:
##            f.write(line)
##        else:
##            new = "|".join(stu_list)+"\n"
##            f.write(new)
##    f.truncate()

studRecLst=["2002224","John  Second "]
##with open("demofile.txt","w") as f:
##    wStr = "|".join(studRecLst)+"\n"
##    f.write(wStr)

####def new_user():
####    newRec = []
####    ID = int(input("ID: "))
####    Name = str(input("Name: "))
####    IC = str(input("IC: "))
####    newRec.append(str(ID))
####    newRec.append(Name)
####    newRec.append(str(IC))
####
####    with open("demofile.txt","a+") as f:
####        wStr = "|".join(newRec)+"\n"
####        f.write(wStr)
####new_user()

with open("demofile.txt","r+") as f:  #read + write 
    f_lines = f.readlines()  #read all into file f
    f.seek(0) #move to position/location 0  of file f (not f_lines)
    for line in f_lines:
        if studRecLst[0] not in line:  # if studRecLst[0]!=line.strip("\n").split("|")[0]
                        #if studID is the first element line after the .split() method/list
            f.write(line)  #put back the same line as there’s no changes
            
    f.truncate()                 #remove the previous set of records
##
