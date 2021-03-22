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
import numpy as np
import re

# A collection of functions to help with text cleaning 
import text_cleaning_helpers as tch
assert tch.date_norm_mmddyy('5-2-1982') == ' may-02-1982 '

# Directories setup
base_dir = os.getcwd()
data_dir = os.path.join(base_dir, 'Data')
stops_dir = os.path.join(base_dir, 'Stops')

# Read in stop words
with open(os.path.join(base_dir, 'stops.txt')) as file:
    stop_words = file.readlines()
    stop_words = [x.strip() for x in stop_words]
    
# For capturing the dates in the text.  I'll try normalization and simply
# replacing by the a marker for a date.
date_mm_dd_yy_forms = re.compile("\d{1,2}[/|.|-]\d{1,2}[/|.|-]\d\d(?:\d\d)?") # take capture group 1
date_month_forms = re.compile("(?:\d+[ |\.|-])?(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[ |\.|-]?(?:\d+[ |\.|-|,]+)?(?:\d{2,4})")    

# Read in the training data
train_df = pd.read_csv(os.path.join(data_dir, r'BBC News Train.csv'))

# text = train_df['Text'][0]
def clean_text(text):
    text = text.lower()










# Basic BOW implementation with Naive Bayes and SVM






# Tensorflow implementation of RNN
# I'll probably use wordnet for embeddings initially as this is a fairly
# simple problem with only 5 classes.  Maybe come back later and see how
# much different using BERT makes.
















