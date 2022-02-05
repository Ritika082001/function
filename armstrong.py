def Total_sum(a,b):
    s = 0
    while(b> 0):
        r = b % 10
        s += (r**a)        
        b //= 10
    return s  
def Number_of_digits(num):   
    c = 0
    while (num>0):
        c+=1
        num//=10
    return c
def isArmstrong(n):
    b = n
    a = Number_of_digits (b)         
    sum_of_digits = Total_sum (a,b) 
    if (sum_of_digits == n):
        return True
    return False
a = int(input("Enter the lower range  :"))
b = int(input("Enter the higher range :"))
print ("The Armstrong numbers in the given range",a, "and",b,"are")
for i in range(a,b+1):
    if(isArmstrong(i)):
        print (i)