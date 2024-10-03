import math as m # imports math library as m

print("problem 1") # answers to problem 1
#definitions
a = 2.3
b = -1.8
c = 4.15

#answer 1
a1 = (a-b)/(a+c) # simple math operations
print("Answer 1:",a1)

#answer 2
a2 = pow(b, 3) + (a*(a+c)) # using pow to raise a number to a power
print("Answer 2:",a2)

#answer 3
a3 = -1*(a*(pow(b,2))) - pow((c/a), (1/3))
print("Answer 3:",a3)

#answer 4
a4 = m.sqrt(pow(a,2) + pow(b,2) + pow(c,2)) # finding the square root with sqrt from math library
print("Answer 4:",a4)

print("\nproblem 2") # answers to problem 2
#definitions
side_a = 8.3
side_b = 6.5
angle_gammaDEG = 40

# a, converting to RADs from DEGs and using sin to find the height
angle_gammaRAD = m.radians(angle_gammaDEG) # converts to RAD python math works in RAD not DEG
height = side_b * m.sin(angle_gammaRAD) # finds height using sin from math library
print("a) height =",height)

# b, using sqrt pow and cos to find side_c
side_c = m.sqrt(pow(side_a,2) + pow(side_b, 2) - 2*side_a*side_b*m.cos(angle_gammaRAD)) # cos form math library 
print("side c =",side_c)

# c, using asin to get angle beta
angle_betaRAD = m.asin(height/side_c) # sin inverse (asin) from math library
angle_betaDEG = m.degrees(angle_betaRAD) # converts from RAD to DEG to print DEG number
print("angle beta =",angle_betaDEG)

# d, using atan to get angle gamma again to double check
angle_gamma2RAD = m.atan(height/(side_a-side_c*m.cos(angle_betaRAD))) # tan inverse (atan) from math library
angle_gamma2DEG = m.degrees(angle_gamma2RAD) # convert to output degrees
print("checking angle gamma again. angle gamma =",angle_gamma2DEG)