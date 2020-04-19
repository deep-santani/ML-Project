# Ploynomial Regression
"""
Aarav is a trying to buy a house and is collecting housing data so that he can estimate the “cost” of the house according to the “Living area” of the house in feet.

Living Area(feet'2) : 2104 1600 2400 1416 3000
Price(100$)         :  400  330  369  232  540
"""
import numpy
from sklearn.metrics import r2_score

Area = [2104,1600,2400,1416,3000]
Price = [400,330,369,232,540]

mymodel = numpy.poly1d(numpy.polyfit(Area, Price, 3))

Area = input("Enter Living Area =")
Area = int(Area)

Price = mymodel(Area)

print(Price) 
