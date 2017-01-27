class milesPerHour():
    def __init__(self, ds=0, hr=0, mn=0):
        self.distance = ds
        self.hours = hr
        self.minutes = mn
        self.mph = 0
    
    def setValues(self, ds, hr, mn):
        self.distance = ds
        self.hours = hr
        self.minutes = mn
        self.mph = 0
        
    def getdist (self):
        return self.distance
    def gethour (self):
        return self.hours
    def getmin (self):
        return self.minutes
    def getmph (self):
        self.mph = self.distance/(self.hours + self.minutes / 60.0)
        return self.mph

def main():
    distance = int(input("Please input the distance"))
    hours = int(input("please input the hours"))
    minutes = int(input("Please input the minutes"))
    speed = milesPerHour(distance, hours, minutes)
    print(speed.getdist(), "miles in",speed.gethour(), "hours and", speed.getmin(),"minutes is", speed.getmph(), "mph" )

    speed.setValues(500, 5, 30)
    print(speed.getdist(), "miles in",speed.gethour(), "hours and", speed.getmin(),"minutes is", speed.getmph(), "mph" )

main()
