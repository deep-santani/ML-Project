#Linear Regression Project
"""
The sales of a company (in million dollars) for each year are shown in the table below.

x (year) 	2005 	2006 	2007 	2008 	2009

y (sales) 	12 	    19 	    29 	     37 	 45

a) Find the least square regression line y = a x + b.
b) Use the least squares regression line as a model to estimate the sales of the company in 2012. 
"""

from scipy import stats

X=[2005,2006,2007,2008,2009]
Y=[12,19,29,37,45]

slope, intercept, r, p, std_err = stats.linregress(X, Y)

def myfun(X):
  return slope * X + intercept

Year = input("Enter Year Which You Gonna to Predict : ") 
Year = int(Year)

Sales = myfun(Year)

print("Estimate Sales in",Year,"is",Sales)

