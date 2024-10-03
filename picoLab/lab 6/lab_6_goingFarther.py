'''
same as the graphing program from task 2 with some changes to th graph data. It ran a lot longer than I thought I would
have it run, so the x axis is in seconds when it likely should have been in minutes.
'''

import matplotlib.pyplot as plt # import matplotlib for graphing

def GetFileData(): # function to read the data in the file line by line

    f = open("thermData.txt", "r") # opens the file in read mode

    x = [] # creates an empty x and y array
    y = []
    k = 0
    for record in f: # reads each line in file using for loop
        record = record.replace("\n", "") # replaces the enter with nothing
        record = record.split("\t") 
        # splits the string into an array of strings at the tab inbetween the two data points
        # can now convert to int and float since \t and \n have been removed
        x.append(int(record[0]))  # convert first part to int and append it to the x array
        y.append(float(record[1])) # convert the second part to a float and append it to the y array
        k=k+1
        
    f.close() # close the file and flush the RAM
    return x, y # return the x and y arrays

def PlotData(x, y): # takes a x and y array and converts it into a graph using pyploy
    plt.plot(x,y, '-o') # plots the x array as the x values and y array as the y values
    plt.title('Temperature Data from the Thermistor Sensor') # adds graph info
    plt.xlabel('Time[s]')
    plt.ylabel('Temperature[°C]')
    plt.grid()
    plt.show() # draw current graph

# Main Program
x, y = GetFileData() # gets data from file by calling GetFileData function, x and y are now arrays
PlotData(x,y) # passes those arrays to PlotData function to create the graph