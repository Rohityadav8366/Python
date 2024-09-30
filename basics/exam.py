def pellindrome(str):
    #reversing the string and save int
    for i in range(0,int(len(str)/2)):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True    
        

str="ramar"
ans=pellindrome(str)
if ans:
    print("pellindrome")
else:
    print("not pellindrome")    

    