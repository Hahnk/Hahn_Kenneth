


def recursion():
    u = input("What is your username?")
    p = input ("What is your password?")
    
    if  u == "username" and p == "password":
        print("Welcome!")
        
    else:
        if  u or p:
            if u == "username":
                print(" password is incorrect")
                recursion()
            elif p == "password":
                print("username is incorrect")
                recursion()
            else:
                print("Both username and password are wrong")
                recursion()

recursion()
