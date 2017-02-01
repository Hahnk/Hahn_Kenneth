#or's must have complete sentences on both sides
st = int(input( 'Please enter your starting number: '))
sz = int(input("Please enter your sequence size:"))
sq = []
for i in range (0,sz):
    if i == 0 or i ==1:
        sq.append(st)
    else:
        sq.append(sq[i-1] + sq[i-2])
    
print(sq)
