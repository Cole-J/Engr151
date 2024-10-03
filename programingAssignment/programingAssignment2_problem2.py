import math as m

'''
'''

def pwmCalc(omg, t): # main function to calculate the duty cycle
    
    y = 5 * m.sin(omg * t) # calcs y
    
    y = (y + 5) / 10 # changes domain to be between 0 and 1
    
    return int(y * pow(2, 16)) # calculates duty cycle and returns it

def p(x): # little function for printing the duty cycle
    print("PWM: %.f" % (x))
    
p(pwmCalc(100, .5))
p(pwmCalc(25, 5.6))
p(pwmCalc(10, 8.7))    
p(pwmCalc(1000,.1))