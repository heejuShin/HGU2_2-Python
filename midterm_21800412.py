#1번
def drawCard(nameTo, mes, nameFrom):
#1-A.
    print("\t",end='')
#3
    if len(nameTo) < 5:
        for i in range(len(nameTo)):
            print(nameTo[i],"-",end='', sep='')
        print("!")
    else:
        print("Dear",nameTo)
#1-B.
    print("")
#1-C.
    count=0
    for ch in mes:
        if count%31==30 and count!=0:
            print(ch)
        else:
            if count==len(mes)-1:
                print(ch)
            else:
                print(ch, end='')
        count+=1
#1-D.
    print("")
#1-E.
    for i in range(31-len("Sincerely yours")):
        print(" ", end='')
    print("Sincerely yours")
    for i in range(31-len(nameFrom)):
        print(" ",end='')
    print(nameFrom)

#2
while 1:
    nameTo=input("Enter the name of the birthday person: ")
    if not (nameTo.isspace() or nameTo == '' or nameTo=='\n'):
        break
    print("One more time ", end='')
#4
message=["Happy birthday!","Count your life by smiles, not tears. Count your age by friends, not years. Happy birthday!","Your birthday is the first day of another 365-day journey. Be the shining thread in the beautiful tapestry of the world to make this year the best ever. Enjoy the ride"]

#5
if len(nameTo)<5 :
    mes=message[0]
elif 5 <= len(nameTo) <10:
    mes=message[1]
else:
    mes=message[2]

#6
while 1:
    nameFrom=input("Enter the sender's name: ")
    if not (nameFrom.isspace() or nameFrom == '' or len(nameFrom)>31):
        break
    print("One more time ", end='')
#7
print("")

#8
drawCard(nameTo, mes, nameFrom)