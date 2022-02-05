def unique_list(l):
    i=0
    x = []
    while i<len(l):
        if l[i] not in x:
            x.append(l[i])
        i=i+1
    print(x)
unique_list([1,2,3,3,3,3,4,5])