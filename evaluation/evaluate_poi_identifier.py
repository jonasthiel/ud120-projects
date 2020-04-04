#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn import tree
from sklearn import model_selection

features_train, features_test, labels_train, labels_test = model_selection.train_test_split(features, labels, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test, labels_test)
acc = clf.score(features_test, labels_test)

i = 0
for j in labels_test:
    if j == 1:
        i += 1      
print("number of POIs in the test set:", i)

print("total people in test set:", len(features_test))

i = 0
for j in range(len(pred)):
    if pred[j] == 1:
        if labels_test[j] == 1:
            i += 1
print("number of true positives:", i)

from sklearn.metrics import precision_score

print("precision of POI identifier:", precision_score(features_test, labels_test, average='weighted'))

from sklearn.metrics import recall_score

print("recall of POI identifier:", recall_score(features_test, labels_test, average='weighted'))

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

i = 0
for j in range(len(predictions)):
    if predictions[j] == 1:
        if true_labels[j] == 1:
            i += 1

print("number of true positives:", i)

i = 0
for j in range(len(predictions)):
    if predictions[j] == 0:
        if true_labels[j] == 0:
            i += 1

print("number of true negatives:", i)

i = 0
for j in range(len(predictions)):
    if predictions[j] == 1:
        if true_labels[j] == 0:
            i += 1

print("number of false positives:", i)

i = 0
for j in range(len(predictions)):
    if predictions[j] == 0:
        if true_labels[j] == 1:
            i += 1

print("number of false negatives:", i)

print("precision of classifier:", precision_score(true_labels, predictions))

print("recall of classifier:", recall_score(true_labels, predictions))


