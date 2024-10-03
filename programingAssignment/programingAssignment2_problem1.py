import math as m

'''
this code has 2 functions, one is the required and the other just helps with test conditions.
the calcSideC function takes the 2 sides and angle by first converting to RADS and then uses tan to get side C,
and then returns the total.
'''

def calcSideC(sideA, sideB, angleY): # pass side a and b and angle y
    # returns an str saying "The perimeter of the triangle is (the total perimeter)"
    sideA = float(sideA) # convert the side variables to floats is they are not already
    sideB = float(sideB)
    angleY = m.radians(angleY) # convert from degrees to radians
    sideC = sideA*m.tan(angleY) # use tan to find the length of side c
    return (sideA + sideB + sideC) # returns the sum of the 3 side variables
    
def p(x): # little function for printing the perimeter and rounding
    print("The perimeter of the triangle is %.2f" % (x)) # rounds to the second decimal

p(calcSideC(4, 6.5, 35)) # test condidtions
p(calcSideC(3.5, 7, 60))
p(calcSideC(5.5, 12.5, 15))
p(calcSideC(5, 7, 45))
