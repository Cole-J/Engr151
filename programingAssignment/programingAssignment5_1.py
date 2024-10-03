import numpy as np
from matplotlib import pyplot as plt

def plot(para_v, para_y, para_thetaArr, para_colorArr, para_resolution = 1, para_x = 0, para_gravity = 9.81):
    # copied from PA4 P2
    distanceArr = [] # creates a distance array and fills it with the distance each projectile travels
    for x in range(len(para_thetaArr)):
        t = para_thetaArr[x] * (np.pi/180) # convert DEG to RADS
        v = para_v
        y = para_y # now we have the t v y and g needed to soolve for distance
        distance = ((v*np.cos(t))/(para_gravity))*((v*np.sin(t))+np.sqrt(pow(v*np.sin(t), 2) + 2 * para_gravity * y)) # distance equals equation
        distanceArr.append(distance) # adds distance to the distance array

    # line plotting
    for x in range(len(para_thetaArr)): # plots each of the lines in the parallel arrays
        t = para_thetaArr[x] * (np.pi/180)
        v = para_v
        y = para_y # defines the t v y along with the g already defined and uses them to find the height at a given x
        d = distanceArr[x] # defines the distance that each projectile travels
        plotX = np.arange(para_x, d, para_resolution)
        plotY = plotX * np.tan(t) - (1/2) * ((pow(plotX, 2) * para_gravity)/(pow(v*np.cos(t), 2))) + y # projectiles height (y) equals equation
        plt.plot(plotX,plotY, para_colorArr[x]) # plots the line

    # creating the legend
    legendArr = []
    for x in range(len(para_thetaArr)):
        string = str(para_thetaArr[x]) + " degree line"
        legendArr.append(string)
    plt.legend(legendArr)

plt.title("graph of projectile trajectories") 
plt.xlabel("distance (m)") 
plt.ylabel("height (m)")

'''
the plot function takes 4 main variables and 3 more can be added.

para_v or start velocity in meters per second

para_y or start y in meters

para_thetaArr or a list of start degrees (length should equal para_colorArr)

para_colorArr or a list of the colors for each line (length should equal para_thetaArr)

para_resolution or the resolution of the graph, by defualt its 1 unit

para_x or start x in meters, by default its 0 meters

para_gravity or gravity in meters per second^2, by default its 9.81 m/s^2
'''

# test case 1
#plot(25, 3.5, [20, 30, 40, 50], ["b", "g", "r", "c"])
# test case 2
plot(25, 3.5, [5, 15, 30, 45, 55, 70], ["b", "g", "r", "c", "m", "y"])
# test case 3
#plot(25, 3.5, [5, 10], ["b", "g"])

plt.show()