def long_list(*list):
    li = []
    for i in list:
        x =len(i)
        li.append(x)
    print(max(li))

long_list ('hii', 'hello', 'welcome', 'me', 'you')