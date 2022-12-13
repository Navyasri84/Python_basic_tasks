'''To find how many elements are present inside the list'''

'''.....first way.....'''

# a=[15,20,35,40,25,45]
# print(len(a))

'''.....second way.....'''
# c=0
# for i in a:
#     c+=1
# print(c)

'''sum of the elements inside the list'''

'''.....first way.....'''

# b=[1,2,3,4]

# print(b[0]+b[1]+b[2]+b[3])
# print(sum(b))

'''.....second way.....'''
# import math
# b=[1,2,3,4]
# print(math.fsum(b))
# print(math.fsum(a+b))

'''sum of numbers'''

'''.....first way.....'''
a=[eval(x) for x in input().split()]
print(sum(a))

'''.....second way.....'''
import math
a=[eval(x) for x in input().split()]
print(math.fsum(a))
