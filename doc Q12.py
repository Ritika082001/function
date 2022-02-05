def a(n):
    n_as_str = str(n)
    if n_as_str == "0":
        return 0
    if n_as_str[-1] == "0":
        print(a(int(n_as_str[:-1])))
    else:
        return n
a(450)
