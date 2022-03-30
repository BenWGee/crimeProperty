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
radius1 = 0.1
radius2 = 0.5
radius3 = 1.0
crimeInR1 = []
crimeInR2 = []
crimeInR3 = []

for indexH, h in houses.iterrows():
    print(indexH)
    countR1 = 0
    countR2 = 0
    countR3 = 0
    for indexC, c in crimes.iterrows():
        dis = dist(h["longitude"],h["latitude"],c["Longitude"],c["Latitude"])
        if dis <= radius3:
            countR3 += 1
            countR2 += 1
            countR1 += 1
        elif dis <= radius2:
            countR2 += 1
            countR1 += 1
        elif dis <= radius1:
            countR1 += 1
    crimesInR3.append(countR3)
    crimesInR2.append(countR2)
    crimesInR1.append(countR1)


houses["Crime 100m"] = crimesInR1
houses["Crime 500m"] = crimesInR2
houses["Crime 1000m"] = crimesInR3
houses.to_csv("houseAndCrimes.csv")
