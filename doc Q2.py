def largest ():
    a=int(input("enter"))
    b=int(input("enter"))
    c=int(input("enter"))
    if a>b and a>c:
        print(a,"largest")
    elif b>a and b>c:
        print(b,"largest")
    elif c>a and c>b:
        print(c,"largest")
largest()