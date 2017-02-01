import random

nums = []
for i in range(1, 10):
    i = nums.append(random.randint(1,101))
print("numbers...")

output = ""    
for num in nums:
    output += (" " + str(num))

def avg(nu):
    avrg = 0
    for num in nu:
          avrg += num
    return (avrg/10)

print(output)
print("\t")
print("The average of the above numbers is....." + str(avg(nums)))


          
