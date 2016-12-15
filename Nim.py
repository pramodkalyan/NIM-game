print("NIM")
win = 0
a,b,c = 15,25,30
def pileChoosen(p):
        temp = p;
        numOfitems = input("Enter number of items you wish to pick :")
        while not numOfitems.isdigit() :
                numOfitems = input("Invalid entry,Enter number of items you wish to pick :")
        numOfitems = int(numOfitems);
        p = p-numOfitems
        while p < 0 or p==temp :
                print("Invalid entry")
                p = pileChoosen(temp)
        return p  
print("Choose a pile,pile names and number of items in it are : a =",a,",b =",b,",c =",c)
invalid=0
while a is not 0 or b is not 0 or c is not 0 :
    pile=0
    while pile is not "a" and pile is not "b" and pile is not "c" :
            pile = input("Choose a pile : ")
            if((pile is "a" and a==0) or (pile is "b" and b==0) or (pile is "c" and c==0)):
                invalid = 1;
                print("Invalid pile")
                continue
            if(pile is "a" and a != 0) :
                a =  pileChoosen(a);
            if(pile is "b" and b!= 0) :
                b = pileChoosen(b);
            if(pile is "c" and c!=0) :
                c = pileChoosen(c);
            if(pile is not "a" and pile is not "b" and pile is not "c") :
                    print("Invalid pile")
    if(invalid==1) :
            invalid=0
            continue
    print("Current pile : ")
    print(a,b,c) 
    length = len(bin(max(a,b,c))[2:])
    list1 = list(bin(a)[2:].zfill(length))
    list2 = list(bin(b)[2:].zfill(length))
    list3 = list(bin(c)[2:].zfill(length))
    listOfall=[list1,list2,list3]
    sumOfbinDigits = [int(list1[i])+int(list2[i])+int(list3[i]) for i in range(length)]
    column,row,foundFirstone,foundOneinCol=0,0,0,0 #intialisation
    if(a==b) :
            listOfall[2] = ['0' for i in range(length)]
    elif(a==c) :
            listOfall[1] = ['0' for i in range(length)]
    elif(b==c):
            listOfall[0] = ['0' for i in range(length)]
    else :
            for digit in sumOfbinDigits :
                if(digit%2 is 1):
                    if(foundFirstone != 1) :
                        for lis in listOfall :
                            row = row+1
                            if(int(lis[column]) == 1) :
                                foundOneinCol = column
                                lis[column] = '0'
                                foundFirstone = 1
                                break
                    elif(foundFirstone==1) :
                        p = foundOneinCol+1 
                        while p is not length :
                            if(int(listOfall[row-1][p]) == 0 and (int(sumOfbinDigits[p])%2 == 1)) :
                                listOfall[row-1][p] = '1'
                            elif(int(listOfall[row-1][p]) == 1 and (int(sumOfbinDigits[p])%2 == 1)):
                                listOfall[row-1][p] = '0'
                            p = p+1
                        break
                column = column+1
    string = ["".join(i)  for i in listOfall ]        
    newValueOfa,newValueOfb, newValueOfc  = int(string[0],2),int(string[1],2),int(string[2],2)
    if((newValueOfa == a) and (newValueOfb == b) and (newValueOfc == c)) :
        win = 1
        if(a is 0 and b is 0 and c is 0):
                break
        if(a is not 0) :
            newValueOfa = a-1;
        elif(b is not 0) :
            newValueOfb = b-1;
        elif(c is not 0) :
            newValueOfc = c-1;
    else :
        win=0
    print("COMPUTERS MOVE-->")
    if(a != newValueOfa) :
            print("Choosen from pile a and number of items choosen :",a-newValueOfa)
    elif(b != newValueOfb) :
            print("Choosen from pile b and number of items choosen :",b-newValueOfb)
    elif(c != newValueOfc) :
            print("Choosen from pile c and number of items choosen :",c-newValueOfc)
    print(newValueOfa,newValueOfb,newValueOfc)
    print()
    a,b,c=newValueOfa,newValueOfb,newValueOfc       
if(win==0) :
    print("YOU LOST !!!! :(")
if(win==1) :
    print("YOU WON CONGRATULATIONS !!!!!!:)")
            
 
    

    
    

    
    
    

