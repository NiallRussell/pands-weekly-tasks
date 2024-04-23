#This program displays a histogram of 1000 random values with a normal distribution, a mean of 5 and a standard deviation of 2
#Author: Niall Russell

#Import matplotlib to allow for plotting
import matplotlib.pyplot as plt
#Import random to allow for random number generation
import random

#Set mean
mu = 5
#Set standard deviation
sigma = 2
#Create list for values
data = []

#Generate 1000 random values
for i in range (1000):
    #Normal distribution with defined mean and SD
    value = random.gauss(mu, sigma)
    #Add each value to list
    data.append(value)

#Plot a histogram of values
plt.hist(data)
#Assign label to x-axis
plt.xlabel("Value")
#Assign label to y-axis
plt.ylabel("Count")
#Assign title
plt.title("Normal distrubution of pseudorandom values")

#Display histogram
plt.show()
