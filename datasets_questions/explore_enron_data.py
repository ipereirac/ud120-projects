#!/usr/bin/python3

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import sys
import joblib
sys.path.append("../final_project/")
from poi_email_addresses import poiEmails


enron_data = joblib.load(open("../final_project/final_project_dataset.pkl", "rb"))

print(len(enron_data))
print(len(enron_data["SKILLING JEFFREY K"].keys()))

count = 0
count_salary = 0
email_address = 0
for person in enron_data:
    if enron_data[person]["poi"]==1:
        count = count +1
    if enron_data[person]["salary"]!='NaN':
        count_salary = count_salary +1
    if enron_data[person]["email_address"]!='NaN':
        email_address = email_address +1
    

print(count)


print(enron_data['PRENTICE JAMES'])

print(enron_data['COLWELL WESLEY'])

print(enron_data["SKILLING JEFFREY K"])

print(enron_data["FASTOW ANDREW S"])

print(enron_data["LAY KENNETH L"])

print(count_salary)
print(email_address)
