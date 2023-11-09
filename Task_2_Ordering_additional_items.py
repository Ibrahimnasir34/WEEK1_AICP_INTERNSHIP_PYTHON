# Initialize selected items and total price
additional_items = []

# Function to calculate the total price based on selected items
def calculate_total_price():
    total = 200.00  # Basic set of components
    for key, value in selected_items.items():
        total += prices[item_codes.index(value)]
    for item in additional_items:
        total += prices[item_codes.index(item)]
    return total

while True:
    print("Do you want to purchase additional items? (Y/N)")
    choice = input()
    if choice.upper() == "Y":
        print("Choose an item from the additional categories:")
        for i in range(8, len(item_codes)):
            print(f"{i - 7}. {descriptions[i]} - ${prices[i]:.2f}")
        choice = input("Enter the number of your choice (1/2/3/4/5/6/7/8 or 0 to finish): ")
        if choice == "0":
            break
        if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            additional_items.append(item_codes[int(choice) + 7])
            print(f"{descriptions[item_codes.index(item_codes[int(choice) + 7)]} added.")
        else:
            print("Invalid input. Please choose a valid item number.")
    elif choice.upper() == "N":
        break
    else:
        print("Invalid input. Please enter Y or N.")

# Output selected items and total price
print("Selected items:")
for key, value in selected_items.items():
    print(f"{descriptions[item_codes.index(value)]}: ${prices[item_codes.index(value)]:.2f}")
if additional_items:
    print("Additional items:")
    for item in additional_items:
        print(f"{descriptions[item_codes.index(item)]}: ${prices[item_codes.index(item)]:.2f}")

total_price = calculate_total_price()
print(f"Total Price: ${total_price:.2f}")
