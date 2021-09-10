#!/usr/bin/python3

import joblib
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = joblib.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]

data_dict.pop('TOTAL',0)

data = featureFormat(data_dict, features)



### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

bonuses_train, salaries_train = targetFeatureSplit(data)
maxxy = max(bonuses_train)

#for k,v in data_dict.items():
#    if v['bonus'] == maxxy:
#        print(k)
#    if v['salary'] == maxxy:
#        print(k)

for k,v in data_dict.items():
    if v['salary'] != 'NaN' and v['bonus'] != 'NaN': #not doing this was causing headache!
        if v['salary'] > 1000000 and v['bonus'] > 5000000:
            print(k)
