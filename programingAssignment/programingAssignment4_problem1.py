import numpy as np
from matplotlib import pyplot as plt

# const variables
x1 = 0 # start of the graph
x2 = 0.04 # end of the graph (the period of the euro standard is 0.02)
res = 0.0001 # resolution of the graph

# t and v variable definition



t1 = np.arange(x1, x2, res)
v1 = 170*np.cos(120*np.pi*t1) # US standard (r)
t2 = np.arange(x1, x2, res)
v2 = 325*np.cos(100*np.pi*t2) # Euro standard (b)

# plt graph plotting

plt.title("Comparison of US vs Euro standard voltage") 
plt.xlabel("time (s)") 
plt.ylabel("voltage (v)") 
plt.plot(t1,v1, "r") # plot red v1 line
plt.plot(t2,v2, "b") # plot blue v2 line

# legend
plt.legend(["US standard", "Euro standard"])

# plot
plt.show()