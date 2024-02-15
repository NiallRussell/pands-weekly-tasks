# This program asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step the next value is calculated by taking the current value and, if it is even, dividing it by two, but if it is odd, multiplying it by three and add one.
# The program ends if the current value is one
#Author: Niall Russell

#Promting use to input a positive integer (using 'number' for user)
a = int(input("Please enter a positive number:"))
#While loop which checks that the integer is positive and reprompts input if not
while a <= 0: 
    #Promting the user to input an integer until it is positive 
    a = int(input("Please enter a positive number:"))
#A list to store calculated values
value_list = []
#While loop which ends if the a is equal to 1
while a != 1:
    #Checking if a is even- after dividing a by 2 it will have no remainder
    if a%2 == 0: 
        #Perform the calculation for even numbers- divide a by 2. Using int to convert to integer as division converts variable to float
        a = int(a/2)
        #Add a to the list
        value_list.append(a)
    #If number is above zero and is not even, it must be odd
    else:
        #Perform the calculation for odd numbers- multiply a by 3 and add 1
        a = (a*3)+1
        #Add a to the list
        value_list.append(a)
print(value_list)
#for loop to print each value in list rather than printing in list format
for value in value_list:
    print(value)