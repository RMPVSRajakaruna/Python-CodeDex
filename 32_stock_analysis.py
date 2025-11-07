# Scope determines where in the program a variable is visible and can be used.

# Here are two types of scope:

# The scope of the answer variable is only inside the add() function. It is a local variable that belongs to the local scope of the add() function.
# Now, a variable created outside of a function is called a global variable and belongs to the global scope, meaning that they can be used by every function.

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56,
                49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
    return stock_prices[x-1]     

def max_price(a, b):
    return max(stock_prices[a-1:b])

def min_price(a, b):
    return min(stock_prices[a-1:b])

print("Price on day 1:", price_at(1))
print("Max price day 5 to 10:", max_price(5, 10))
print("Min price day 10 to 20:", min_price(10, 20))
