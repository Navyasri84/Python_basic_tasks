'''Area of Circle from the user input'''

'''............first way.........'''

# r=eval(input("Enter the radius:"))
# pi=22/7
# area=(pi)*r**2
# print("Area of the circle with radius "+str(r)+" is: %.2f"%area)

'''............second way.........'''
import math
r=eval(input("Enter the radius:"))
area=math.pi*r**2
print("Area of the circle with radius "+str(r)+" is: %.2f"%area)


