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
    elif voterAge>=18 and voterAge<60 :
        print("Voter is Adult:") 
    else:
        print("Voter is seniour Citisen:")           


def moviesTickets():
    watcherAge=int(input("Enter the age:"))
    day=input("Enter the day:")
    if day=="wednesday":
        if watcherAge<18:
            print("The age of watcher is :",watcherAge," movie ticket is $8 afetr discount $2:you should pay $6")
        else:
             print("The age of watcher is :",watcherAge," movie ticket is $12 afetr discount $2:you should pay $10")    
    else:
        if watcherAge<18:
            print("The age of watcher is :",watcherAge," movie ticket is $8:you should pay $8")
        else:
             print("The age of watcher is :",watcherAge," movie ticket is $12:you should pay $12")



def tocheckPalindrome():
    str=input("Enter the string: ")
    ref={}
    for ch in str:
        ref[ch]=ref.get(ch,0)+1
    noOdd=0
    for i in ref.values():
        if i%2==1:
            noOdd+=1
    if noOdd<=1:
        print("possible to make pelindrome:") 
    else:
        print("Not possible to make pelindrome:")               


# dictionary taking from user
def dic():
    n=int(input("Enter the size of dictionary:"))
    dic={}
    for i in range(n):
        k=int(input("Roll.number: "))
        v=input("Enter the name of Student: ")
        dic[k]=v
    
    print(dic)    

# list taking from user
def list():
    n=int(input("Enter the size of list: "))
    list=[]
    for i in range(n):
        list.append(int(input()))
    print(list)    

# tuple taking from user
def tupleUser():
    n=int(input("Enter the size of tuple: "))
    tuple1=tuple((int(input())) for i in range(n))
        
    print(tuple1)

# Set value taking by user
def setUser():
    n=int(input("Enter the size of set: "))
    set={int(input()) for i in range(n)} 
    print(set)


def set1():
    n=int(input("enter the size: "))
    set2=set()
    for i in range(n):
        set2.add(int(input()))
    print(set2)


def armstrong(n):
    a=len(n)
    
