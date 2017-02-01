w = input("Please enter a word")
sto = len(w)

def tree(w,sta,sto):
    if sta <= sto:
        print("{:>20}".format(w[0:sta]))
        tree(w,sta+1,sto)

tree(w,0,sto)
