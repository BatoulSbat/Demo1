# Create a list of menu items
menu = ["Coffee", "Tea", "Sandwich", "Cake"]

# Create a dictionary of stock values for each item
stock = {
    "Coffee": 100,
    "Tea": 50,
    "Sandwich": 20,
    "Cake": 30
}

# Create a dictionary of prices for each item
price = {
    "Coffee": 2.50,
    "Tea": 1.50,
    "Sandwich": 5.00,
    "Cake": 3.00
}

# Calculate total stock worth
total_stock_worth = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

# Print the result
print("Total stock worth in the café:", total_stock_worth)
