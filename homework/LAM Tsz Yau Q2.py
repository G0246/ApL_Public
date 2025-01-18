# Define the variable
snacks = input("Do you want some snacks? (yes/no): ") # Ask the child

# Using if-statement to see the input
if snacks == "yes":                               # If the child want snacks
    choice = input("Enter your choice (ice-cream / cookies / candies): ")
    if choice == "ice-cream":                     # If choice is ice-cream
        print("Remember to wash your hands.")     # Print the ouput
    elif choice == "cookies":                     # If choice is cookies
        print("Can you share with your friends?") # Print the ouput
    elif choice == "candies":                     # If choice is candies
        print("Don't eat too much.")              # Print the ouput
elif snacks == "no":                              # If the child doesn't want snacks
    print("Good! Let's play games instead.")