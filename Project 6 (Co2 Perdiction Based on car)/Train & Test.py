
import numpy
import pandas 
from sklearn.metrics import r2_score
numpy.random.seed(2)


df = pandas.read_csv("E:/3.Extra Education/ML Project/Project 6 (Co2 Perdiction Based on car)/Car.csv")

X = df['Volume']
Y = df['CO2']

train_x = X[:27]
train_y = Y[:27]

test_x = X[27:]
test_y = Y[27:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(test_y, mymodel(test_x))

Volume=input("Volume of Car :")
Volume=int(Volume)

print("The Predicated CO2 Maybe :",mymodel(Volume)) 