
def harshad(num):
    sum = rem = 0
    while num > 0:
        rem = num % 10
        sum = sum + rem
        num = num// 10
    return sum
num = int(input("Enter the Number = "))
sum = harshad(num)
print("The Sum of the Digits =",sum)
if num % sum == 0:
    print(num,"is a Harshad Number.")
else:
    print(num,"is not harshad number")