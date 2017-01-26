class car():
    def __init__(self, p = "", i= "", e= "", t= ""):
         self.paint = p
         self.interior = i
         self.engine = e
         self.tires = t

    def custom(self, p = "", i= "", e= "", t= ""):
         self.paint = p
         self.interior = i
         self.engine = e
         self.tires = t
         
    def getpaint(self):
        return self.paint
    def getinterior(self):
        return self.interior
    def getengine(self):
        return self.engine
    def gettires(self):
        return self.tires

def main():
    paint = input("Please input paint")
    interior = input("Please input interior")
    engine = input("Please choose engine")
    tires = input("Please choose tires")
    new = car(paint, interior, engine, tires)
    print("Your Car is ready! \n Paint: \t",car.getpaint(),"\n Interior: \t",car.getinterior(), "\n Engine: \t",car.getengine(),"\n Tires: \t",car.gettires())

main()
