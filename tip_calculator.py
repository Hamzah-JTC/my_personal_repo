# Tip Calculator
# Greetings

print("Hello there and welcome to Hamzah's Tip Calculator!")

# Cost of the food: Begin with an input statement (value) and store it within a variable
# The input statement is set to a type float so that the user can input decimaled numbers such as: 15.25 
# I chose an if/elif/else statement to account for the vast possiblities of inputs including addressing inputs that could possible break my code.

# Do not forget to add the sales tax of 10%

cost_of_food = float(input("What was the cost of your (hopefully) delicious meal?: $"))
if cost_of_food == 0: # setting this variable to zero insures that this unlikely input is covered
    print(f'The cost of your food is free!!')
elif cost_of_food > 0: # The most possible input from the user
    print(f'The total cost of food is ${cost_of_food}')  
else:
    print("I do not understand your input! Please input the numerical cost of your food!") 
    # the else statement covers the possiblity of the user input being a data type other than an integer or float.

# Add in sales tax: declared a variable for sales tax and then multiplied the initial cost of food by the sales tax variable. I declared a new variable that will hold the value of the cost of food multiplied by the sales tax.

sales_tax = 1.10
total_cost_minus_tips = round((cost_of_food * sales_tax ), 2)
# I learned this 'round'function technique in the code below from programiz.com. I set the decimal place to 2 in order to account for the floated cost of food being between 0.01 - 0.99. You will see me using it several times within this app.
print(f'The total cost of your meal with tax included is: ${total_cost_minus_tips}')

# Percentage of the tip: First I need to ask the user for permission in order to factor in a tip. 
# Once again I chose an if/elif/else statement to cover the possiblities of user inputs.
# A 'yes' or 'no' input is logical for gaining permission from the user.
# The choose_tip variable needs to have a floated value in order to address the possiblity that the user will input a decimaled tip amount.
# I chose to nest another if/elif/else statement within my initial if statement in order to cover the specific tip input possibilities.
# Next: Add an input statement (value) and store it within a variable. In order to keep the code from breaking I am adding an if statement.

tip_consent = input("Would you like to add a tip for your server? Input: 'y' or 'n': ")
if tip_consent == 'y':
    print("Sounds good! I am happy to assist you in calculating your tip!")
    choose_tip = float(input("Choose the tip amount, in dollars, that you would like to add to the meal cost before taxes.\nNote: Input a dollar amount:$ "))
    tip_percentage = round(( choose_tip / cost_of_food) * 100, 2) # rounding to 2 is the most practical when dealing with money
    if choose_tip >= 0.01: # I wanted to cover the possibility of the user wanting to tip a single cent or more.
        print(f'You chose ${choose_tip} for a tip which amounts to a {round(tip_percentage, 2)}% tip added to the cost of the meal before taxes.') # I thought it would be more practical to ask the user to input an amount of money rather than asking the user what specific tip percentage they would you like to give. I believe that most people are not comfortable dealing with percentages without a calculator at hand.
        bill_and_tip_total = round((total_cost_minus_tips + choose_tip), 2) # The cost of the meal and sales tax with tip included.
        print(f'The total cost of the bill with tips is ${round(bill_and_tip_total, 2)} ')
    elif choose_tip <= 0:
        print("It looks like you changed your mind! There will be no tip after all!!")
        print(f'The total cost of the bill without tips is ${round(total_cost_minus_tips, 2)}')
    else:
        print("I do not understand your input! Please try again by inputing a numerical dollar amount!")
elif tip_consent == 'n': 
    print("I understand...let us move on to discuss how many people will be splitting the bill!")
    # I thought that it would be a good idea to periodically update the user on their cost.
    print(f'The total cost of the bill without tips is ${round(total_cost_minus_tips, 2)}')
else:
    print("I do not understand your input! Please try again and input either 'y' or 'n': ")

# Number of people splitting the bill: Begin with an input statement (value) and store it within a variable.
# Even in the case of counting the amount of people that are splitting the bill I chose to float my input variable. As illogical as this may sound, a user may justify inputing, for instance, 2.5 people are splitting the bill. 

num_splitting_bill = float(input("How many total people will be involved with splitting the bill? "))
if num_splitting_bill <= 1: # <= 1 addresses the user inputing zero or a negative number or the more rational input of 1 to declare that they are the only person paying.
    # Nested if/else statements are necessary to differentiate between those who split a bill with tips included and those who split a bill without tips
    if tip_consent == 'y':
        print(f'There is no need to split the bill. Your total cost is ${round(bill_and_tip_total, 2)}')
        # nested if/else statements addresses  
    elif tip_consent == 'n':
        print(f'There is no need to split the bill. Your total cost is ${round(total_cost_minus_tips, 2)}')
elif num_splitting_bill >= 2: # >= 2 people splitting the bill being a very probable outcome.
    # As above the nested code differentiates between the two possible bill splitting possibilities
    if tip_consent == 'y':
        print(f'The total number of people splitting the bill is {num_splitting_bill}')
        # the simple division of the bill and tip total divided by the number of people splitting the bill (along with rounding to two decimal places) will accurately convey the individual bill of each person.
        share_of_bill = round((bill_and_tip_total / num_splitting_bill), 2)
        print(f'Each person will evenly pay ${share_of_bill}') # a final printout of the individual bill(s)
    elif tip_consent == 'n':
        print(f'The total number of people splitting the bill is {num_splitting_bill}')
        share_of_bill = round((total_cost_minus_tips / num_splitting_bill), 2)
        # notice how the value of the variable "share_of_bill" changes based on whether user chooses to pay tips or not.

print("Thank you for using Hamzah's Tip Calculator!")