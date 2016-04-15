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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

sum1 = 0

count = 0

lmax = 1
lmin = 999999

for i in enron_data:
    if enron_data[i]['salary'] != 'NaN' and enron_data[i]['salary'] != 0:
        if enron_data[i]['salary'] < lmin:
            lmin = enron_data[i]['salary']
        if enron_data[i]['salary'] > lmax:
            lmax = enron_data[i]['salary']
 
print lmax
print lmin       
#print count

#print len(enron_data)
#percent = count/float(len(enron_data))
#print percent
