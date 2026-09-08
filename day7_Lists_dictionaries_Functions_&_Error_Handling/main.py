# 1. Defining a structure (Dictionary)

product_item = {
    "name": "Notebook",
    "price": 2.50,
    "availability": "active"
}
print(product_item)




# 2.Exercise 1: Write a function that calculates a total. (Creating a Function with Try/Except to handle bad inputs safely)
def calculate_item_total(price, quantity_str):
    try:
        # Convert string input to integer safely
        quantity = int(quantity_str)
        if quantity < 0:
            return 0.0 #simple validation rule

        return price * quantity 
    except ValueError:
        print("Error: Quantity must be valid Number!")
        return 0.0

# 3. Using the function
total = calculate_item_total(product_item["price"], "3")
print(f"Total: ${total}")  # Output: Total: $7.5

def calculate_total(price, quantity):
    try:
        quantity = int(quantity)
        if quantity < 0:
            print("Error: Quantity cannot be negative")
            return 0.0
    except ValueError:
        print("Error: Quantity must be a valid number")
        return 0.0
    
    total = price * quantity
    return total

# --- Test it out ---
print(calculate_total(2.50, "3"))      # Works! Outputs: 7.5
print(calculate_total(2.50, "three"))  # Safely handles error! Outputs: 0.0
