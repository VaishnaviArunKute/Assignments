def check(str):
    if len(str) % 4 == 0:
        print(str[::-1])
    else:
        print(str)

check("hel")
