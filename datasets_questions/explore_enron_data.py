#!/usr/bin/python

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

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print("number of data points in the Enron dataset", len(enron_data))

print("number of features per person in the Enron dataset", len(enron_data['METTS MARK']))

counterPOI = 0
for i in enron_data.keys():
    if enron_data[i]["poi"] == 1:
        counterPOI += 1
print("number of POIs in the Enron dataset", counterPOI)

print("total value of the stock belonging to James Prentice", enron_data["PRENTICE JAMES"]["total_stock_value"])

print("number of messages from Wesley Colwell to POIs", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print("value of stock options exercised by Jeffrey K Skilling", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

keyPeople = ["SKILLING JEFFREY K", "LAY KENNETH L", "FASTOW ANDREW S"]
h = 0
for i in keyPeople:
    if enron_data[i]["total_payments"] > h:
        h = enron_data[i]["total_payments"]
        j = i
print("from Lay (chairman), Skilling (CEO) and Fastow (CFO), the following person took home the most money:", j)
print("total payments to", j,"amount to:", enron_data[j]["total_payments"])

counterSalary = 0
counterEmail = 0
for i in enron_data.keys():
    if enron_data[i]["salary"] != "NaN":
        counterSalary += 1
    if enron_data[i]["email_address"] != "NaN":
        counterEmail += 1
print(counterSalary, "persons have a quantified salary in the Enron dataset")
print(counterEmail, "persons have an email address associated in the Enron dataset")

counter = 0
for i in enron_data.keys():
    if enron_data[i]["total_payments"] == "NaN":
        counter += 1
print(counter, 'people have "NaN" for their total payments')
print(round((counter / len(enron_data.keys())), 2), 'percentage of people have "NaN" for their total payments')

counter = 0
for i in enron_data.keys():
    if enron_data[i]["poi"] == "1":
        if enron_data[i]["total_payments"] == "NaN":
            counter += 1
print(counter, 'POIs have "NaN" for their total payments')
print(round(counter / counterPOI), 'percentage of POIs have "NaN" for their total payments')


