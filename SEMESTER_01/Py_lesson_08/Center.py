w1 = input ("Please input word 1")
w2 = input ("Please input word 2")
w3 = input ("Please input word 3")

def makeCenter(w):
    if len(w) >= 20:
        return (w)
    else:
        return makeCenter (" "+ w +" ")

print (makeCenter(w1))
print (makeCenter(w2))
print (makeCenter(w3))
