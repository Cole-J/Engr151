import math as m

# main function
def sqrt(x, iterations):
    approx = x/2.0 # first approximation
    for i in range(iterations): # runs for as many iterations as the user wants using for loop
        better = (approx + x/approx)/2.0 # makes an approximation
        approx = better
    error = (m.sqrt(x) - approx)/m.sqrt(x)
    error = m.fabs(error) * 100 # converts error float to a percent error
    return (approx, error) # returns a tuple with the approx of the sqrt and the error compared to the actual sqrt

# test cases
case1 = sqrt(64.0, 4)
print("case 1: approx " + str(case1[0]) + " error " + str(case1[1]) + "%")
case2 = sqrt(64.0, 8)
print("case 2: approx " + str(case2[0]) + " error " + str(case2[1]) + "%")
case3 = sqrt(37.0, 5)
print("case 3: approx " + str(case3[0]) + " error " + str(case3[1]) + "%")
case4 = sqrt(25.0, 1)
print("case 4: approx " + str(case4[0]) + " error " + str(case4[1]) + "%")