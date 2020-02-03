
import random

nosofpoints = 2000
textboxeslimit = 200
filename = "datasetsize" + str(nosofpoints) + ".txt"
datafile = open(filename , "w+")

for i in range(nosofpoints):
    datapoint = set()
    pointlength = random.randrange(textboxeslimit/4, 0.9*textboxeslimit)
    for j in range(pointlength):
        datapoint.add(random.randrange(1 , textboxeslimit))
    datapoint = list(datapoint)
    datapoint.sort()
    datafile.write(str(datapoint))
    datafile.write("\n")