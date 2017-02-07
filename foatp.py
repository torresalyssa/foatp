# Using classification techniques for first-order automated theorem proving.

import numpy as np 
import pandas as pd 

print 'reading in training dataset...'
train_df = pd.read_csv('./dataset/train.csv', header=None, sep=',')

print 'reading in testing dataset...'
test_df = pd.read_csv('./dataset/test.csv', header=None, sep=',')



