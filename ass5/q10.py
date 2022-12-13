sal = float(input(("enter your salary: ")))
year = int(input("enter your years of service: "))
if year > 5:
    new_sal = sal*(1+0.05)
    print("your salary with bonus is ",new_sal)
else:
    print("you didn't get the bonus") 