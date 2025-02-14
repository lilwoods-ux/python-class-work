"""
in built group]==
"""
from dataclasses import replace

#string functions
text = "hello world"
print(len(text)) #the ethod len it returna the length of the string
print(text.upper()) #the upper converts the string into caps
print(text.lower()) #thhe lower converts the string into lower case letters
replacetext = text.replace("hello","timothy")
print(text)# replace replace's texts/
print(text.split())

## INTEGERS GROUP
pos_num = 10
neg_num = -20
float_num = 10.33
print(abs(neg_num))#returns the positive version of the number
print(pow(2,3))# 2^3 = 2 * 2 * 2 = 8
print(divmod(10,3))# (3,1) quotient and reminder are returned as a tuple
print(round(float_num,1)) # 10.3
print(sum([pos_num, float_num])) # 10.33 and 10

##LISTS
nums = [3,1,2,4,5]
print(len(nums)) # returns the number of items in the list
print(list(reversed(nums))) # reverses the list
print(min(nums)) # min number in the list is returned
print(max(nums))# returns maximum number
nums.append(10)
print(nums)
print(nums.pop()) # removes and returns the last item in the list



















