#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
#You should create a function called <tt>sqrt</tt> that does this.
#I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
#This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 
#This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.

#$ python squareroot.py
#Please enter a positive number: 14.5
#The square root of 14.5 is approx. 3.8.

#https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
#defining function
def sqrt(): 
    #promting input of number
    number = float(input("Please enter a positive number:"))
    #first guess will be at least half the value of the number
    nth_guess = number/2
    #define a number of iterations- I could not find a consensus online as to how many
    for i in range (10):
        #Newtown's formula
        nth_guess = (nth_guess + (number/nth_guess))/2 
    #print solution
    print(f'The square root of {number} is approx. {nth_guess}')
#calling the function
sqrt()
