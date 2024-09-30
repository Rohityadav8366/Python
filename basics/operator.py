def large():
    a=input("Enter the val of A:")
    b=input("Enter the value of B:")
    c=input("Enter the value of C:")
    if a>b and a>c:
        print("a is greter rthen b and c")   
    elif b>c:
        print("b >a ,c")    
    else:
        print("c is greater then a,b")    

def Star():
    #str=input("Enter the string :")
    for i in range(1,10):
        for j in range(1,i*2):
           print(" ",end="")
        for j in range(i,10):
            print("*",end="")
        
        print()        


def pet():
    for i in range(1,10):
        for j in range(1,i):
            print("*",end="")
        print() 

def D():
    for i in range(1,10):
        for j in range(1,10):
            if (i==1 and j==9)or(i==9 and j==9):
                print(" ",end="")
            elif i==1 or j==1 or i==9 or j==9 :
                print("* ",end="")
            else:
                print(" ",end="")
        print()

def ageCatogori():
    voterAge=int(input("Enter the of age "))
    if voterAge <=13:
        print("Vopter is child:")
    elif voterAge <18:
        print("Voter is teenager:")
    elif voterAge>=18:
        print("Voter is Adult:") 
    else:
        print("Voter is seniour Citisen:")           
ageCatogori()        