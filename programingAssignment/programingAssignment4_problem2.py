import numpy as np
from matplotlib import pyplot as plt

# variables to change
#              parallel arrays, the same index of each array is the information for the same projectile
thetaInit =    [30, 45, 60] # degrees
velocityInit = [25, 25, 25] # m/s
yInit =        [3.5, 3.5, 3.5] # m
lineColors =   ["r", "g", "b"] # colors of the lines
legend =       ["30 degrees", "45 degrees", "60 degrees"] # what the legend says about each line
g = 9.81 # the acceleration from gravity

distanceArr = [] # creates a distance array and fills it with the distance each projectile travels
for x in range(len(thetaInit)):
    t = thetaInit[x] * (np.pi/180) # convert DEG to RADS
    v = velocityInit[x]
    y = yInit[x] # now we have the t v y and g needed to soolve for distance
    distance = ((v*np.cos(t))/(g))*((v*np.sin(t))+np.sqrt(pow(v*np.sin(t), 2) + 2 * g * y)) # distance equals equation
    distanceArr.append(distance) # adds distance to the distance array

# graph const variables
start = 0
res = 1 # resolution of the graph

# plt graph
plt.title("graph of projectile trajectories") 
plt.xlabel("distance (m)") 
plt.ylabel("height (m)")

# line plotting
for x in range(len(thetaInit)): # plots each of the lines in the parallel arrays
    t = thetaInit[x] * (np.pi/180)
    v = velocityInit[x]
    y = yInit[x] # defines the t v y along with the g already defined and uses them to find the height at a given x
    d = distanceArr[x] # defines the distance that each projectile travels
    plotX = np.arange(start, d, res)
    plotY = plotX * np.tan(t) - (1/2) * ((pow(plotX, 2) * g)/(pow(v*np.cos(t), 2))) + y # projectiles height (y) equals equation
    plt.plot(plotX,plotY, lineColors[x]) # plots the line

# legend
plt.legend(legend)

# plot
plt.show()