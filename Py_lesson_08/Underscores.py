senten = input("Please input a sentence")

def repl(sent):
    if sent.count(" ") == 0:
         return sent
    else:
         return sent[0 : sent.index(" ")] + "_" + repl(sent[sent.index(" ")+1 : len(sent)])
print(repl(senten))
    
