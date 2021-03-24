# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 2021

@author: Geoff

BBC News Datasets Text Classification (Topic Labeling)

Text documents are one of the richest sources of data for businesses.
We’ll use a public dataset from the BBC comprised of 2225 articles, each
labeled under one of 5 categories: business, entertainment, politics, 
sport or tech.
The dataset is broken into 1490 records for training and 735 for testing. 
The goal will be to build a system that can accurately classify previously 
unseen news articles into the right category.

The competition is evaluated using Accuracy as a metric.

To download data, please see:
https://www.kaggle.com/c/learn-ai-bbc/data
"""

import os
import pandas as pd
import re
import string

from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn import metrics

# A collection of functions to help with text cleaning 
import text_cleaning_helpers as tch

# Functionality checks
assert tch.date_norm_mmddyy('5-2-1982') == ' may-02-1982 '

# Directories setup
base_dir = os.getcwd()
data_dir = os.path.join(base_dir, 'Data')
stops_dir = os.path.join(base_dir, 'Stops')

# Read in stop words
with open(os.path.join(stops_dir, 'stops.txt')) as file:
    stop_words = file.readlines()
    stop_words = [x.strip() for x in stop_words]
    
# For capturing the dates in the text.  I'll try normalization and simply
# replacing by the a marker for a date.
date_mm_dd_yy_forms = re.compile("\d{1,2}[/|.|-]\d{1,2}[/|.|-]\d\d(?:\d\d)?") # take capture group 1 if normalizing format
date_month_forms = re.compile("(?:\d+[ |\.|-])?(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[ |\.|-]?(?:\d+[ |\.|-|,]+)?(?:\d{2,4})")    

# Read in the training data
train_df = pd.read_csv(os.path.join(data_dir, r'BBC News Train.csv'))

#############################
# Cleaning Setup
#############################

def remove_punc(text):
    return ''.join([x for x in text if x not in string.punctuation])

def replace_dates(text):
    temp = re.sub(date_mm_dd_yy_forms, 'date', text)
    temp = re.sub(date_month_forms, 'date', temp) 
    return temp

def remove_stops(text):
    return [x for x in text if x not in stop_words]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def text_stemmer(text):
    return [stemmer.stem(x) for x in text]

def text_lemmatizer(text):
    return [lemmatizer.lemmatize(x) for x in text]


# Testing Purposes
# test = 'i love july 4, 1982 and the awesome days. do you LOVE !!! the holidays'
# remove_punc(test)    
# replace_dates(test)
# test = word_tokenize(test)
# remove_stops(test)


############################
# Text Cleaning
############################

def text_cleaning(df, text_normalization = 'None'):
    df['Text'] = df['Text'].apply(lambda x: remove_punc(x))
    df['Text'] = df['Text'].apply(lambda x: x.lower())
    df['Text'] = df['Text'].apply(lambda x: replace_dates(x))
    df['Text'] = df['Text'].apply(lambda x: word_tokenize(x))
    df['Text'] = df['Text'].apply(lambda x: remove_stops(x))
    
    if text_normalization == 'Stem': df['Text'] = df['Text'].apply(lambda x: text_stemmer(x))
    if text_normalization == 'Lemmatize': df['Text'] = df['Text'].apply(lambda x: text_lemmatizer(x))
    
    df['Text'] = df['Text'].apply(lambda x: ' '.join(x))
    
    return df

############################
# Basic BOW implementation with a couple of classifiers
############################

train_clean = text_cleaning(train_df)

vectorizer = CountVectorizer(ngram_range=(1,1))
vectorizer.fit(train_clean['Text'])
bow = vectorizer.transform(train_clean['Text'])

# Split data
X_train, X_test, y_train, y_test = train_test_split(bow, train_clean['Category'], test_size =0.25, random_state = 42)

# Selection of Classifiers
classifier = MultinomialNB().fit(X_train, y_train)
classifier = LogisticRegression().fit(X_train, y_train)
classifier = DecisionTreeClassifier().fit(X_train, y_train)
classifier = SVC().fit(X_train, y_train)

predicted = classifier.predict(X_train)
print(f"Accuracy: {metrics.accuracy_score(y_train, predicted)}")
print(metrics.confusion_matrix(y_train, predicted))

# Tensorflow implementation of RNN
# I'll probably use wordnet for embeddings initially as this is a fairly
# simple problem with only 5 classes.  Maybe come back later and see how
# much different using BERT makes.

