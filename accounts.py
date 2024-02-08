
# Defining a function which checks if account number is 10 digits long. If so, it runs through each digit and replaces the digit with an "X" if the digit is in position 0-5. 
# If number inputted is not 10 digits long, it prints error message
def inputnumber():
    # Prompting the user to input their number
    fullnumber = input("Please enter a 10 digit account number: ")
    # Converting the string to a list to allow for cycling through items
    listnumber = list(fullnumber)
    # If length of list is 10 then replace the first 6 digits with "X", if not equal to 10 then print error message
    if len(listnumber) == 10:
        # For loop to cycle through items in the list
        for i, v in enumerate(listnumber):
            # If item position is 5 or less (first position in the list is 0)
            if i <= 5:
                # Change the corresponding digit to "X"
                listnumber[i] = "X"
        # Convert the list back to a string for readability when printing        
        xnumber = ''.join(listnumber)
        # Print the encoded number
        print(xnumber)
    # If length of number is not equal to 10, print error message                    
    else:
        print("Number must be 10 digits long")

#Calling the function        
inputnumber()


