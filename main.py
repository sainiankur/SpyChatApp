print("hello")
print("welcome to the spychat")
spy_exist = raw_input("are you already exist Y or N?")
if spy_exist.upper() == "Y":
    print("already existing spy")
    choice = True
    while(choice):
        spy_choice = input("enter 1 for update status or 2 for exit")
        if spy_choice==1:
            spy_status = raw_input("enter your status")
            print spy_status
        elif spy_choice==2:
            print "you are log out"
            choice =False
        else:
            print "invalid choice please enter 1 and 2"


elif spy_exist.upper() == "N":
    spy_name = raw_input("enter your name")
    if len(spy_name) >= 3:
        print spy_name
        salutaion=raw_input("mr or miss")
        spy_name = salutaion+" "+spy_name
        print spy_name
        spy_age = input("enter your age")
        if spy_age >= 12 and spy_age <= 50:
            print "you are eligible to be spy"
            print spy_age
            spy_ratings = input("enter your rating")
            if spy_ratings >= 4.0 and spy_ratings >= 5.0:
                print "very good spy"
            elif spy_ratings >= 3.0 and spy_ratings <= 4.0:
                print("good spy")
            else:
                print("bad spy")
        else:
            print "you are not eligible to be spy"

    else:
        print "invalid"
else:
    print "invalid choice"
