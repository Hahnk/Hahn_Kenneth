import random
class User:
    def __init__(self, fName= "", lName= "", avat=""):
       self.firstName = fName
       self.lastName = lName
       self.avatar = avat
       self.userID = random.randint(0, 100000000)

    def __str__(self):
        return "Customer Info...\nFirst Name: " + self.firstName + \
                           "\nLast Name: " + self.lastName + \
                           "\nAvatar: " + self.avatar + \
                           "\nUser ID#: " + str(self.userID)
def main():
    fName = input("Please input your First name")
    lName = input("Please input your Last name")
    choice = input("Would you like to use a public avatar? (y or n)")
    if choice == "n":
            user1 = User(fName,lName)
    if choice == "y":
            avat = input("Please input your avatar name")
            user1 = User(fName,lName,avat)

    print(user1)
    

main()
