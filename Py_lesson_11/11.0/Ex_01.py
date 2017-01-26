class milesPerHour():
    def __init__(self, ds = "", hr= "", mn=""):
        self.distance = ds
        self.hours = hr
        self.minutes = mn
        mph = 0
    
    def setValues(self, ds = "", hr= "", mn=""):
        self.distance = ds
        self.hours = hr
        self.minutes = mn
        mph = 0
        
    def getdist (self):
        return self.distance
    def gethour (self):
        return self.hours
    def getmin (self):
        return self.minutes
    def getmph (self):
        mph = (int(self.distance)/(int(self.hours+self.minutes)/ 60.0))
        return mph

def main():
    distance = input("Please input the distance")
    hours = input ("please input the hours")
    minutes = input("Please input the minutes")
    speed = milesPerHour(distance, hours, minutes)
    print(speed.getdist(), "miles in",speed.gethour(), " is", speed.getmph(), "mph" )

    speed.setValues(500, 5, 30)
    print(speed.getdist(), "miles in",speed.gethour(), " is", speed.getmph()," mph")

main()
