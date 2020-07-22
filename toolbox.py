# -*- coding: cp65001 -*-
import arcpy

layer1 = arcpy.GetParameterAsText(0)  

time2score = ['5',"10","15","20",'0']
tempscore = [40,30,20,10,50]
time2score_dict = {}
for i in range(5):
    time2score_dict[time2score[i]] = tempscore[i]


def score_caulculator(time1,time2):
    total = 0
    if time1 != None:
        total+= time2score_dict[str(int(time1))] * 1.5
    else:
        total += 0
    if time2 != None:
        total += time2score_dict[str(int(time2))]/2
    else:
        total += 0
    return total



places = arcpy.UpdateCursor(layer1)
for place in places:
    time1 = place.Min_ToBreak
    time2 = place.Min_ToBreak_1

    total =  score_caulculator(time1, time2)

    place.score = total

    places.updateRow(place)
