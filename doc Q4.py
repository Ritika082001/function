def string_reverse(str1):

    reverse_str1 = ''
    index = len(str1)
    while index > 0:
        reverse_str1+=str1[ index - 1 ]
        index = index - 1
    print(reverse_str1)
string_reverse('1234abcd')