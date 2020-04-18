# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:35:43 2020

@author: vaibhav
"""

import requests
from input_data import data_in

URL = 'http://127.0.0.1:5000/predict'

headers = {'Content-Type': 'application/json'}

data = {'input': data_in}

r = requests.get(URL,headers=headers,json=data)

r.json()


