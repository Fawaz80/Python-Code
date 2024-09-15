# List of fruits with prices
fruits = [
    ("Apple", 10),
    ("Orange", 8),
    ("Banana", 3),
    ("Strawberry", 6),
    ("Kiwi", 12),
    ("Pineapple", 20)
]


for index, (fruit, value) in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Unused variable
index = 0

# Ask the user to enter a number between 1 and 6
try:
    input = int(input("Enter the number of the fruit, from 1 to 6: "))
except ValueError:
    print("Invalid input! Please enter a number.")


if 1 <= input <= 6:
    # Get the value associated with the entered index
    selected_value = fruits[input - 1][2]  # Error: Index 2 doesn't exist
    print(f"The value associated with the selected fruit is: {selected_value}")
else:
    print("Invalid input. Please enter a number between 1 and 6.")

# Another unused function (dead code)
def function():
    print("Welcome to the program, we will show the price of the chosen fruit.")
