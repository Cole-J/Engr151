from framework import create_traffic_light

mainLight = create_traffic_light(15,14,13) # pins that the LEDs are on, for args goes r, y, g

mainLight.GO() # turns on just the green led

mainLight.SLOW() # turns on just the yellow led

mainLight.STOP() # turns on just the red led