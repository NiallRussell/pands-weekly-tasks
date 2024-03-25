#This program takes a positive floating-point number as input and outputs an approximation of its square root
#Author: Niall Russell

#Using Newton's method for estimating square roots: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
#Defining function
def sqrt(): 
    #Promting input of number
    number = float(input("Please enter a positive number:"))
    #First guess will be at least half the value of the number
    nth_guess = number/2
    #Define a number of iterations- I could not find a consensus online as to how many, 
    #however, this source suggests that 7 iterations is enough to produce more than 60 accurate digits- https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
    for i in range (7):
        #Newtown's formula
        nth_guess = (nth_guess + (number/nth_guess))/2 
    #Print solution
    print(f'The square root of {number} is approx. {nth_guess}')
#Calling the function
sqrt()
