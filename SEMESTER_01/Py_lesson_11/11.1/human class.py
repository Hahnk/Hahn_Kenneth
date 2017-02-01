class human:
    def __init__(self, hair = "", eyes = "", skin = ""):
        self.h = hair
        self.e = eyes
        self.s = skin

    def man(self, hair = "", eyes = "", skin = ""):
        self.h = hair
        self.e = eyes
        self.s = skin

    def gethair(self):
        return self.h
    def geteyes(self):
        return self.e
    def getskin(self):
        return self.s
def main():
    h = input("Please input hair color")
    e = input("Please input eye color")
    s = input("Please input skin color")
    humin = human(h,e,s)
    print ("My info....\n Hair:", h, "\nEyes:", e, "\nSkin:", s)

main()
