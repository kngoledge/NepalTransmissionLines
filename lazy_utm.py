import pandas as pd
import numpy as np 
import utm

#download csv, must be located in same folder as this script
data = np.loadtxt('utmNepal.csv',dtype='str',delimiter=',')

#mild csv formatting
east = data[:,1]
north = data[:,2]
east = east.tolist()
del east[0]
north = north.tolist()
del north[0]

#lists to accumulate and store lat and long
all_lat = []
all_long = []

#calculate all conversions
for x in range(len(east)):
    latlon = utm.to_latlon(float(east[x]), float(north[x]), 45, 'R')
    #returns tuple
    all_lat.append(latlon[0])
    all_long.append(latlon[1])

#create dataframe
all_data = [('lat', all_lat),
           ('lon', all_long)
           ]
df = pd.DataFrame.from_items(all_data)

#create csv
df.to_csv('latlonNepal.csv', sep=',', header=True, index=False)
