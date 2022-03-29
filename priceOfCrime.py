"""
@overview: A script to report the number of crimes within n meters
of each property in the area. Script will calculate the correlation
between the two variables.

@author: Bengee
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geopy.distance

#===============================================================================
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
#===============================================================================

#===============================================================================
def dist(lon1,lat1,lon2,lat2):
    try:
        coords1 = (lon1, lat1)
        coords2 = (lon2, lat2)
        return geopy.distance.geodesic(coords1, coords2).km
    except:
        return 1000
#===============================================================================

crimes = pd.read_csv("Crime_Baltimore.csv")
crimeLoc = crimes.filter(["Longitude","Latitude"], axis=1)
houses = pd.read_csv("propertyDataCondensed.csv")
radius = 0.1
crimesInArea = []

for indexH, h in houses.iterrows():
    print(indexH)
    count = 0

    for indexC, c in crimes.iterrows():
        dis = dist(h["longitude"],h["latitude"],c["Longitude"],c["Latitude"])
        if dis <= radius:
            count += 1
    crimesInArea.append(count)


houses["CrimeArea"] = crimesInArea
houses.to_csv("houseAndCrimes.csv")
title = "Plot of Crimes Within 100m VS Property Price"
xLab = "Number of Crimes Within 100m"
yLab = "Property Price"
makePlot(list(houses["CrimeArea"]),list(houses["price"]),title,xLab,yLab)
