# This program prompts the use to input two money amounts in cent, and prints the sum of these amounts in euro and cent

#Prompting user to input first amount
amount1 = int(input("Input first amount (in cent): "))
#Prompting user to input second amount
amount2 = int(input("Input second amount (in cent): "))
#Adding amount1 and amount2 together
sum = amount1 + amount2
#Calculating whole euro amount
eurosum = sum//100
#Calculating remaining cents
centsum = sum%100
#Combining euro and cent
totalsum = str(f"€{eurosum}.{centsum}")
#Printing the solution
print("The sum of these is "+ totalsum)