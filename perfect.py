
def perfect_number():
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
        print(sum,"perfect")
    return sum == n
n=int(input("enter"))
perfect_number()