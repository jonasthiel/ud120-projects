#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

### Initial features_list
#features_list = ['poi','salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees', 'to_messages', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi']

features_list = ['poi', 'total_payments', 'total_stock_value', 'from_poi_to_this_person', 'to_messages_poi_share', 'from_messages_poi_share']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "rb") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
data_dict.pop('THE TRAVEL AGENCY IN THE PARK', 'TOTAL')

### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_dict

for i in my_dataset:
    if my_dataset[i]['from_this_person_to_poi'] != 'Nan' and my_dataset[i]['from_messages'] != 'NaN':
        my_dataset[i]['to_messages_poi_share'] = int(my_dataset[i]['from_this_person_to_poi']) / (int(my_dataset[i]['from_messages']) + int(my_dataset[i]['from_this_person_to_poi']))
    else:
        my_dataset[i]['to_messages_poi_share'] = 'NaN'
    if my_dataset[i]['from_poi_to_this_person'] != 'NaN' and my_dataset[i]['to_messages'] != 'NaN':
        my_dataset[i]['from_messages_poi_share'] = int(my_dataset[i]['from_poi_to_this_person']) / (int(my_dataset[i]['to_messages']) + int(my_dataset[i]['from_poi_to_this_person']))
    else:
        my_dataset[i]['from_messages_poi_share'] = 'NaN'

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
#clf = GaussianNB()

from sklearn import tree
#clf = tree.DecisionTreeClassifier()

from sklearn.svm import SVC
#clf = SVC()

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

#clf = GaussianNB()

clf = tree.DecisionTreeClassifier(max_features=2, min_samples_split=2, criterion='entropy')

#clf = SVC(kernel='rbf', C=10000)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
