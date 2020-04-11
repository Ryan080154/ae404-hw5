# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 11:15:52 2020

@author: Home
"""

import requests
url = "https://www.books.com.tw/"
data =requests.get(url)
print(data)

print(data.text)