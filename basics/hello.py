print("Hello python first code")
def prime(n):
    count=0
    if n==1:
        print(n,"Co-prime")
    else:   
        for i in range(2,(n)//2):
            if n%i==0:
                count+=1
        if count==0:
            print("prime",n)
        else:
            print("Not prime",n)

def fectorial(n):
    fect=1
    for i in range(1,n+1):
        fect*=i
    print("Fectorial of",n,":",fect)
fectorial(6)
