def volume (w,l,h) :
    return ((w*l*h)/1728)

w = int(input("Please enter width"))
        
l = int(input("Please enter length"))
      
h = int(input("Please enter Height"))

print ( "Your Volume in Cubic Feet is{:<0.3f}" .format (volume(w,l,h) ))
