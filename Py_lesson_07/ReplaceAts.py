sant = input("Please input a sentence")
lop = 0
def replace():
    sent = sant
    while lop < sent.count("a") > 0:
       sent = sent[0 : sent.index("a")] + "@" + sent[sent.index("a")+1 : len(sent)]
    print( "A time...." + sent)

replace()


