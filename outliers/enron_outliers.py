#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
highestBonus = 0
for i in data_dict.keys():
    if data_dict[i]["bonus"] == "NaN":
        continue
    else:
        if int(data_dict[i]["bonus"]) > highestBonus:
            highestBonus = data_dict[i]["bonus"]
            name = i
print("biggest outlier in the Enron dataset:", name)

data_dict.pop("TOTAL", 0)

nameList = []
for i in data_dict.keys():
    if data_dict[i]["bonus"] == "NaN":
        continue
    else:
        if int(data_dict[i]["bonus"]) >= 5000000:
            if data_dict[i]["salary"] == "NaN":
                continue
            else:
                if data_dict[i]["salary"] > 1000000:
                    nameList.append(i)
print("additional outlier in the Enron dataset", nameList)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


