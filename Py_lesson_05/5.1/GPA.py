g1=input(" What is your first grade?")
g2=input(" what is your second grade?")
g3=input(" What is your thrid grade?")
g4=input(" what is your forth grade?")
g5=input(" what is your fifth grade?")
g6=input(" what is your sixth grade?")

def calcp(grd):
    if grd == "A":
        return 4.0
    if grd == "B":
        return 3.0
    if grd == "C":
        return 2.0
    if grd == "D":
        return 1.0
    if grd == "F":
        return 0.0
    else:
        print( "Please Capitalize all your grades")
    
print("your GPA is: ", float(calcp(g1)+calcp(g2)+calcp(g3)+calcp(g4)+calcp(g5)+calcp(g6))/6)
