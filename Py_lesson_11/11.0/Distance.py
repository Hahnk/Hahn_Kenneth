import math
class Distance:
    def __init__(self, x1 ="", y1 ="", x2= "", y2 =""):
        self.xo = x1
        self.yo = y1
        self.xt = x2
        self.yt = y2
        self.distance = 0

    def setvalues(self, x1 ="", y1 ="", x2= "", y2 =""):
        self.xo = x1
        self.yo = y1
        self.xt = x2
        self.yt = y2
        self.distance = 0

    def getmph(self):
        self.distance = math.sqrt(int(self.xt-self.xo)*int(self.xt-self.xo)+int(self.yt-self.yo)*int(self.yt-self.yo))
        return self.distance
        
def main():
    x1 = int(input("Please input X1"))
    y1 = int(input("Please input Y1"))
    x2 = int(input("Please input X2"))
    y2 = int(input("Please input Y2"))

    dis = Distance( x1, y1, x2, y2)
    
    print("Distance = ", dis.getmph()) 
    

main()

#{:<0.2f}.format
