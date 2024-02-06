#Enter amount1(in cent): 65
#Enter amount2(in cent): 180
#The sum of these is €2.45

#Prompting user to input first amount
amount1 = int(input("Input first amount (in cent): "))
#Prompting user to input second amount
amount2 = int(input("Input second amount (in cent): "))
#Adding amount1 and amount2 together
sum = amount1 + amount2
#Calculating whole euro amount
eurosum = sum//60
#Calculating remaining cents
centsum = sum%60
#Combing euro and cent
totalsum = str(f"€{eurosum}.{centsum}")
#Printing the solution
print("The sum of these is "+ totalsum)