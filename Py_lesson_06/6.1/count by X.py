mx= int(input("Please input maximum"))
mn= int(input("please input  multiple"))
lne = ""

for i in range(0,mx+1,mn):
    lne = lne + str(i) + "\t"
print(lne)


