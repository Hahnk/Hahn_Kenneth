nums = [2,6,8,9,10,12,13,15,17,24,55,66,78,77,79]

def gfactor (number):
    for i in range (2, number):
        if (number%i) == 0:
            return 1
        else:
            return 0
def remoprimes():
    for number in nums:
        if gfactor(number)==0:
            nums.remove(number)
remoprimes()
print(nums)
