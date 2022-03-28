"""
@overview: A script to report the number of crimes within n meters
of each property in the area. Script will calculate the correlation
between the two variables.

@author: Bengee
"""

import pandas as pd
import matplotlib.pyplot as plt

#====================================================================
def makePlot(x,y,title,xLab,yLab):
    """
    Overview: Make a plot of x vs y
    """
    plt.plot(x,y)
    plt.title(title)
    plt.xlabel(xLab)
    plt.ylabel(yLab)
    plt.xlim(x[0],x[len(x) -1])
    plt.ylim(min(y),max(y))
    plt.grid()
    plt.show()
#====================================================================
