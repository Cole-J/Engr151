import math as m

def invcos(x, quad):
    r = m.degrees(m.acos(x))
    match quad: # using match case to get around if elif else
        case 1: # cases for different quads
            return r
        case 2:
            return 180 - r # angle is less than 180 going clockwise
        case 3:
            return -1 * r + 360 # angle is more than 180 going counterclockwise
        case 4:
            return 360 - r # angle is less than 360 going counterclockwise
        case _:
            print("error: %i is an invalid quadrant" % (quad))

def p(str, invcos): # function to reduce number of print statements
    print(f"{str}: %.2f" % (invcos))
    
p("test 1",invcos(-.5,3))
p("test 2",invcos(.5,4))
       
p("\ncase 1",invcos(m.sqrt(3)/2,4))
p("case 2",invcos(-1*m.sqrt(3)/2,2))
p("case 3",invcos(-.25,3))
p("case 4",invcos(0,2))