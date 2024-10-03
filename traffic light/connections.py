'''
traffic signal cases

main traffic light green by default

main street adjacent crosswalk is off unless irq
if the main street is green then the adjacent cross walk will turn on otherwise put in a request
if the main street turns green and there is a crosswalk request also turn on the adjacent crosswalk

if there is a request for the opposite street to be green
check that main street has been open for 120 seconds
if so then open the opposite street

if there is an irq for the adjacent cross walk send a request
when the opposite street is open next turn on the opposite streets adjacent cross walk

if there is an irq for the opposite streets bike lane and its been 120 seconds since main streets been open
close main street and open opposite street


connections

connect fsr and ultra
street and crosswalk semi connected

requests

main street defualt every thing else closed
proxy allows the main crosswalk to also be open

ultra and fsr request that main street closes and opposite street opens
proxy allows opposite crosswalk to also be open

main adjacent crosswalk button
close opposite street
open main crosswalk
proxy closes opposite street and adjacent crosswalk

opposite adjacent crosswalk button
close main street
open opposite crosswalk
proxy closes main street and adjacent crosswalk




'''

import time
c = 0
s = 0
while True:
    
    
    
    
    if c % 50 == 0:
        s += 1
        print(f"{s}")
        

    
    
    time.sleep(.02)
    c += 1
    
    
    
    
    