import math as m

'''
the different output cases for the problem
vs > .6 r vs - 0.6
vs <= .6 r 0
vs < -vbr r -999
'''

def vl(vs, vbr): # function to find the vl from vs and vbr
    if (vs < -vbr): # checks for a diode failure first
        return -999
    elif (vs > .6): # checks lower bound
        return vs - 0.6
    elif (vs <= .6): # checks upper bound
        return 0
    
def p(c, vl): # function to make printing easier
    print(f"case {c}: VL: %.2f" % (vl))
    
p(1,vl(5,75))
p(2,vl(0.23,100))
p(3,vl(-65,50))
p(4,vl(1,-2))