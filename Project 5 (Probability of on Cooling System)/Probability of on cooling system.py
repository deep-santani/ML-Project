# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:34:23 2020
Temp,Humidity,Gas,Probability
@author: deep
"""

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("E:/3.Extra Education/ML Project/data.csv")

X = df[['Temp', 'Humidity' ,'Gas']]
y = df['Probability']

scaledX = scale.fit_transform(X)


regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

Temp = input("Enter Temperature:")
Temp =int(Temp)

Humidity = input("Enter Humidity:")
Humidity =int(Humidity)

Gas = input("Enter Gas:")
Gas =int(Gas)

scaled = scale.transform([[Temp, Humidity, Gas]])

Probability = regr.predict([scaled[0]])
print("The Probability of Cooling System on Maybe",Probability,"%") 