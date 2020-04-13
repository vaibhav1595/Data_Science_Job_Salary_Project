# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:24:02 2020

@author: vaibhav
"""

# Data Libraries
import pandas as pd 
import numpy as np 

# Visualization Libraries
import matplotlib.pyplot as plt

# Import Dataset
f = pd.read_csv('model_buidling.csv')

# Info about the dataset
f = f.drop(columns = 'Unnamed: 0',axis = 1)
f.info()

# Build a 'model' dataframe with relevant columns from 'f' dataframe
f_model = f[['avg_salary','Rating','Size','Type of ownership','Industry','Sector',
             'Revenue','job_state','same_state','age','python','spark','aws',
             'excel','role','seniority','R','sql']]

# Create dummy variables 
f_dummy = pd.get_dummies(f_model)

# Regression Analysis
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score


X = f_dummy.drop('avg_salary', axis =1)
y = f_dummy['avg_salary'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

# OLS regression analysis
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()

# Linear regression analysis

lr = LinearRegression()
lr.fit(X_train, y_train)
np.mean(cross_val_score(lr,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))

# Lasso Regression analysis

lm = Lasso(alpha=.13)
lm.fit(X_train,y_train)
np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))

alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3)))
    
plt.plot(alpha,error)

err = tuple(zip(alpha,error))
df_err = pd.DataFrame(err, columns = ['alpha','error'])
df_err[df_err.error == max(df_err.error)]

# Random Forest 

rf = RandomForestRegressor()
np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 3))

# tune models GridsearchCV 
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error',cv=3)
gs.fit(X_train,y_train)

gs.best_score_
gs.best_estimator_

# test ensembles 

lml = Lasso(alpha=.13)
lml.fit(X_train,y_train)

tpred_lm = lm.predict(X_test)
tpred_lml = lml.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,tpred_lm)
mean_absolute_error(y_test,tpred_lml)
mean_absolute_error(y_test,tpred_rf)

mean_absolute_error(y_test,(tpred_lm+tpred_rf)/2)





















