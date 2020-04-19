# Predict_Data_Science_Job_Salary_Project 

## Project from Scratch on Salary Prediction for Data Science Job Roles posted on Glassdoor.com

- Developed a tool estimating the salary for the position of data science job with **[MEAN ABSOLUTE ERROR (MAE) ~ $13k]** posted on glassdoor.com in the United States
- Scraped over 1000 Jobs lists from glassdoor using python and selenium
- Performed Exploratory Data Analysis to uncover the underlying important structure of the glassdoor job dataset
- Engineered features from the text of each job description to quantify the value companies put on python, sql, R, spark, aws and excel
- Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model
- Built a client facing API using flask

# Resources 

- **Python Version: 3.7**
- **Packages**: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask,pickle, json
- **For Web Framework Requirements**: pip install -r requirements.txt
- **Scraping Glassdoor using Selenium Github**: https://github.com/arapfaik/scraping-glassdoor-selenium
- **Scraping Glassdoor using Selenium Article**: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
- **Productionize a Machine Learning model with Flask Article**: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Data Collection / Web Scraping Data Science Job Roles posted on Glassdoor.com using Selenium
### Parameters Scraped
- Job title
- Salary Estimate
- Job Description
- Rating
- Company
- Location
- Company Headquarters
- Company Size
- Company Founded Date
- Type of Ownership
- Industry
- Sector
- Revenue
- Competitors

## Data Cleaning

Cleaned the data scraped from glassdoor.com to make the data usable for our model. In addition, I made the following modifications which produced the following variables:

- Removed the rows with no Salary Estimate content
- Parsed the numeric data out of the Salary Estimate
- Made columns for Employer Provided Salary and Hourly wages
- Parsed company ratings from company name
- Creation of a new column with a condition of whether the work was at the company headquarters
- Transformed the Company Founded Date data to Company Age data
- Parsed various skills listed in the job description
  - python
  - sql
  - R
  - spark
  - aws
  - excel
- Creation of a new column with Simplified Job Role and Level of Seniority

## Exploratory Data Analysis (EDA)
- Performed EDA - https://github.com/vaibhav1595/Data_Science_Job_Salary_Project/blob/master/Exploratory%20Data%20Analysis.ipynb

## Buidling a Model
- Built a dataframe for our model with relevant columns 
- Transformed the categorical variables into dummy variables. In addition, splitted the data in train and test set
- Performed Regression analysis using Linear Regression, Lasso Regression and Random Forest
  - **Linear Regression**: to create a baseline for our model
  - **Lasso Regression & Random Forest**: As their was sparcity associated with the data, in my view these models match well
  
## Model Performance
- **Random Forest**: MAE = 13.12
- **Lasso Regression**: MAE = 18.42

## Productionize a Machine Learning model
Final Stage: In this stage, I created an endpoint of the flask API, which was hosted on a local webserver.The API endpoint takes a request from a work posting with a list of values and returns an approximate salary.
