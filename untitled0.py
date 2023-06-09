# -*- coding: utf-8 -*-
"""
Created on Fri May  5 14:51:42 2023

@author: kp272
"""
from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#from sklearn.externals import joblib
#!pip install joblib

df= pd.read_csv("spam.csv", encoding="latin-1")
df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
	# Features and Labels
df['v1'] = df['v1'].map({'ham': 0, 'spam': 1})
X = df['v2']
y = df['v1']
	
	# Extract Feature With CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(X) # Fit the Data
    
pickle.dump(cv, open('tranform.pkl', 'wb'))
    
    
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
	#Naive Bayes Classifier
#from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf.fit(X_train,y_train)
clf.score(X_test,y_test)
filename = 'nlp_model.pkl'
pickle.dump(clf, open(filename, 'wb'))
    
#Alternative Usage of Saved Model
#joblib.dump(clf, 'NB_spam_model.pkl')
#NB_spam_model = open('NB_spam_model.pkl','rb')
#clf = joblib.load(NB_spam_model)

