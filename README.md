# NepalTransmissionLines
converting UTM coordinates to decimal degrees and stitching these coordinates together to determine Nepal transmission lines

# Python 3
uses packages numpy, pandas, and utm (Bidirectional UTM-WGS84 converter! Thank you, developers!)

# Updates
Stanford UTM -> decimal degree conversion is in place!
First time around, the utm coordinates were extracted from scanned pdf using online web resources. I am hoping to automate this, alongside the geovisual stitching.

# TLDR
Input: PDF with at least 1 table of Standard UTM coordinates (for now, I'll build in UTM->decimal degree, but later will create options for the geospatial data handling, i.e. if the coordinates are already in decimal degree or degrees, minutes, seconds) 
Output: geospatial visualization of the plotted coordinates! (edges and analytics not yet included, but look forward)
