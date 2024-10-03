import numpy as np
from matplotlib import pyplot as plt

# main function
def plot(para_v, para_y, para_thetaArr, para_colorArr = [], para_resolution = 1, para_x = 0, para_gravity = 9.81):
    legendArr = []
    # line plotting
    for x in range(len(para_thetaArr)): # plots each of the lines in the parallel arrays
        theta = para_thetaArr[x] * (np.pi/180) # gets the current theta from the array and converts from degrees to rads
        # calculate the distance the projectile travels
        distance = ((para_v*np.cos(theta))/(para_gravity))*((para_v*np.sin(theta))+np.sqrt(pow(para_v*np.sin(theta), 2) + 2 * para_gravity * para_y))
        # create the x array (x values go from the start or para_x to the end which is distance with a resolution of para_resolution)
        plotX = np.arange(para_x, distance, para_resolution)
        # a y array in terms of x array
        plotY = plotX * np.tan(theta) - (1/2) * ((pow(plotX, 2) * para_gravity)/(pow(para_v*np.cos(theta), 2))) + para_y # projectiles height (y) equals equation
        if len(para_colorArr) > 0:
            plt.plot(plotX,plotY, para_colorArr[x]) # plots the line with the given color
        else:
            plt.plot(plotX, plotY) # plots the line with a random color

        # creates a legend string with the template ({degree} degree line)
        string = str(para_thetaArr[x]) + " degree line"
        legendArr.append(string) # adds the line to the legend array

    plt.legend(legendArr) # creates the legend using legend array

# graph setup
plt.title("graph of projectile trajectories") 
plt.xlabel("distance (m)") 
plt.ylabel("height (m)")

'''
the plot function takes 4 main variables and 3 more can be added.

para_v or start velocity in meters per second

para_y or start y in meters

para_thetaArr or a list of start degrees (length should equal para_colorArr)

para_colorArr or a list of the colors for each line (length should equal para_thetaArr), 
by default its [] and it will choose random colors

para_resolution or the resolution of the graph, by defualt its 1 unit

para_x or start x in meters, by default its 0 meters

para_gravity or gravity in meters per second^2, by default its 9.81 m/s^2

below are the test cases. uncomment what you want to view
'''

# test case 1
#plot(25, 3.5, [20, 30, 40, 50])
# test case 2
plot(25, 3.5, [5, 15, 30, 45, 55, 70])
# test case 3
#plot(10, 3.5, [85, 90], ["c", "m"], .00001)

plt.show()