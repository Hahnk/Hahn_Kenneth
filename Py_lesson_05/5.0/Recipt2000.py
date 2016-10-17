i1 = (input( " Please input Item 1"))
p1 = float(input (" please input the price" ))
i2 = (input("Please input item 2"))
p2 = float(input (" please input the price"))
i3 = (input (" please input Item 3"))
p3 = float(input (" please input the price"))

subt = ( p1 + p2 + p3 )

if subt >= 2000 :
            disc = (subt* .15)

if subt < 2000:
           disc = 0
disubt = (subt - disc)          
tax = (disubt* .08) 
total = (tax + disubt)

print ("<<<<<<<<<<< Receipt >>>>>>>>>>>>>>")
def frmat ( i, p ):
        print (" {:<10}.......{:.2}".format(i,p))

frmat (i1, p1)
frmat (i2, p2)
frmat (i3, p3)
       
