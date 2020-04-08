# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:05:46 2020

@author: vaibhav
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/vaibhav/Desktop/DS Projects/Glassdoor Project/chromedriver"

df = gs.get_jobs('data scientist', 1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)