# his is a concept that trips up a lot of people, so definitely practice and practice. 💪

# In this chapter, we learned:

# The "Don't Repeat Yourself" methodology.
# We've been using built-in functions like print() and input() all along.
# How to define and call a function – the two-step process.
# Inputs with parameters and arguments.
# Outputs with the return keyword.
# Function scope vs. global scope.
# Here's the function skeleton one more time, just in case you forget!

# def function_name(parameter1, parameter2):
#   # The code inside
#   return value


menu = ["🍔 Cheeseburger", "🍟 Fries", "🥤 Soda", "🍦 Ice Cream", "🍪 Cookie"]

def welcome():
    print("👋 Welcome to the Snack Shop!")
    print("Here is our menu:")
    for i in range(len(menu)):
        print(str(i+1) + ". " + menu[i])

def order(x):
    if x > 0 and x <= 5:
        return menu[x-1]
    else:
        return "Invalid input."

welcome()
choice = int(input("Enter your choice: "))
print(order(choice))
