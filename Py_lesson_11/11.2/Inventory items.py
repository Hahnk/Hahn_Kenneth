import random
class Inventory_Item:
    def __init__(self, man = "", nam = "", cat = "", prc = 0):
        self.manu = man
        self.name = nam
        self.catg = cat
        self.ucps = random.randint(0, 10000000000000)
        self.prce = prc

    def __str__(self):
        return "Item info\n Manufacturer:" + self.manu + \
                           "\n Name: " + self.name + \
                           "\ncategory: " + self.catg + \
                           "\nUSC: " + str(self.ucps) + \
                            "\nprice:" + str(self.prce)

def main():
    name = input("Please input the name")
    manu = input("Please input the manufacturer")
    choice = input ("Will you be entering category and price information?")
    if choice == "n":
        item1 = Inventory_Item(name, manu)
    else:
        catg = input("Please input the category")
        prc = int(input("Pleae input the price"))
        item1 = Inventory_Item(name, manu, catg, prc)
        
    print(item1)
main()
        
