choice = input("Would you like to go on an adventure!?!?! a or b for yes or no ")

if choice == "a":
    choice = input("What kind!?! Small?(a) or Big?(b)")
    if choice == "a":
        choice = input("Wait! when do you want to leave? later(a)? or never(b)? ")
        if choice == "a":
            print("Alright, see you later!")
        else:
            print ("...oh, ok...see you then...")
    else:
        choice = input(" BIG!?@!?@?#?@? HOW BIG??? Endless(a) or unachievable? (b)")
        if choice == "b":
            print ("Oh well....why start what you can't finish...?")
        else:
            print (" Awesome! Its such an endless adventure, you already completed it before you started!")
else:
    choice = input("....oh....Will I be able to change your mind...?")
    if choice == "y":
        choice = input(" REALLY!?!?!?!?")
        if choice == "y":
            print(" HOORAY!!! THANK YOU!!!")
        else:
            print("...oh...")
    else:
        choice = input ("Are you REALLLLLLY SUUURE????")
        if choice  == "y":
            print (" Oh, ok... Have a good day ")
        else:
            print(" SO...wait...no meaning yes or...?")
       
