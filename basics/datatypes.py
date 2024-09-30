
def prime(n):
    count=0
    if n==1:
        print(n,"Co-prime")
    else:    
        for i in range(2,n//2):
            if n%i==0:
                count+=1
        if count==0:
            print("Prime number")
        else:
            print("Not prime nuber")
prime(1)