def positive():
    list1 = [10, -21, 4, -45, 66, -93, 1]
    pos_count=0
    neg_count=0
    i=0
    while i<len(list1):
        if list1[i]>= 0:
            pos_count += 1
        else:
            neg_count += 1
        i=i+1
    print("Positive numbers in the list: ", pos_count)
    print("Negative numbers in the list: ", neg_count)
positive()