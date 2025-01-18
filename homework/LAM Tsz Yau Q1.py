# Define the variables
price1 = float(input("Enter a price: "))       # Input and float the first price
price2 = float(input("Enter another price: ")) # Input and float the second price

# Price comparasion
if price1 > price2: # Check if the first one larger than the second one?
    print("The first price is larger than the second one.") # Print the output
elif price1 < price2: # Check if the first one smaller than the second one
    print("The first price is smaller than the second one.") # Print the output
elif price1 == price2: # Check if they are the same value.
    print("The prices are the same.") # Print the output