#def recurCount (to, curr, by):
 #   if curr > to:
 #       return to
  #  else:
   #     print (curr)
    #    return recurCount (to, curr+by, by)
#recurCount(to, curr+by, by)
print("------------------------------------------------------------")

word = input("Please enter a word")

def wordBox(word, num):
   if(num >= len(word)):
       return ""
   else:
       print(word)
       wordBox(word, num + 1)

wordBox(word, 0)

print("------------------------------------------------------------")


number = int(input("Please enter a number: "))

def recur(number):
   if(number == 0):
       return 1
   else:
       return number * recur(number - 1)

print(recur(number))


print("------------------------------------------------------------")

