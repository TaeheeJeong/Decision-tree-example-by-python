# Decision_tree 
# week1 assignment
"""
Created on Mon May 09 10:30:45 2016

@author: taehee Jeong
"""

import pandas as pd
#import numpy as np

#%%Load the dataset

AH_data = pd.read_csv("C:/Bigdata/Machine learning for Data Analysis/wk1/tree_addhealth.csv")

data_clean = AH_data.dropna()

data_clean.dtypes
data_clean.describe()

# features and target
predictors = data_clean[['BIO_SEX','HISPANIC','WHITE','BLACK','NAMERICAN','ASIAN',
'age','ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail','DEP1',
'ESTEEM1','VIOL1','PASSIST','DEVIANT1','SCHCONN1','GPA1','EXPEL1','FAMCONCT','PARACTV',
'PARPRES']]

targets = data_clean.TREG1

#%%Split into training and testing sets
from sklearn.cross_validation import train_test_split
pred_train, pred_test, tar_train, tar_test  =   train_test_split(predictors, targets, test_size=.4)

pred_train.shape
pred_test.shape
tar_train.shape
tar_test.shape

#%% Build a decision tree model
from sklearn.tree import DecisionTreeClassifier

#Build model on training data
classifier=DecisionTreeClassifier()
classifier=classifier.fit(pred_train,tar_train)

# apply decision tree model to get prediction for test data
predictions=classifier.predict(pred_test)

import sklearn.metrics
# Confusion Matrix
#              +---------------------------------------------+
#              |                Predicted label              |
#              +----------------------+----------------------+
#              |          (+1)        |         (-1)         |
#+-------+-----+----------------------+----------------------+
#| True  |(+1) | # of true positives  | # of false negatives |
#| label +-----+----------------------+----------------------+
#|       |(-1) | # of false positives | # of true negatives  |
#+-------+-----+----------------------+----------------------+
sklearn.metrics.confusion_matrix(tar_test,predictions)

# Accuracy
accuracy = sklearn.metrics.accuracy_score(tar_test, predictions)
print "Test Accuracy: %s" % accuracy

#%%Displaying the decision tree

# after install graphviz
#pip uninstall pyparsing
#pip install -Iv https://pypi.python.org/packages/source/p/pyparsing/pyparsing-1.5.7.tar.gz#md5=9be0fcdcc595199c646ab317c1d9a709
#pip install pydot

from sklearn import tree
#from StringIO import StringIO
#from io import StringIO
from sklearn.externals.six import StringIO  
#from StringIO import StringIO <- makes error
out_data = StringIO()
tree.export_graphviz(classifier, out_file=out_data)

#from IPython.display import Image
import pydotplus
graph=pydotplus.graph_from_dot_data(out_data.getvalue())
#Image(graph.create_png())
graph.write_pdf("C:\Bigdata\Machine learning for Data Analysis\wk1\decision_tree.pdf") 

#%% Some example 
##############################
##############################
#from sklearn.datasets import load_iris
#from sklearn import tree
#iris = load_iris()
#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(iris.data, iris.target)
#
#from sklearn.externals.six import StringIO  
#import pydot 
#dot_data = StringIO() 
#tree.export_graphviz(clf, out_file=dot_data) 
#graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
#graph.write_pdf("iris.pdf") 
