# Define arrays to store item information
item_codes = ["A1", "A2", "81", "82", "B3", "C1", "C2", "C3", "D1", "D2", "E1", "E2", "EB", "F1", "F2", "G1"]
descriptions = ["Compact Case", "Tower Case", "8 GB RAM", "16 GB RAM", "32 GB RAM", "1 TB HDD", "2 TB HDD", "4 TB HDD",
                "240 GB SSD", "480 GB SSD", "1 TB HDD (2nd)", "2 TB HDD (2nd)", "4 TB HDD (2nd)", "DVD/Blu-Ray Player",
                "DVD/Blu-Ray Re-writer", "Standard OS", "Professional OS"]
prices = [75.00, 150.00, 79.99, 149.99, 299.99, 49.99, 89.99, 129.99, 59.99, 119.99, 49.99, 89.99, 129.99, 50.00,
          100.00, 100.00, 175.00]

# Initialize selected items and total price
selected_items = {"Case": "", "RAM": "", "Main HDD": ""}
total_price = 200.00  # Basic set of components

# Input and validation for Case
while True:
    print("Choose a case:")
    for i in range(2):
        print(f"{i + 1}. {descriptions[i]} - ${prices[i]:.2f}")

    choice = input("Enter the number of your choice (1/2): ")
    if choice in ["1", "2"]:
        selected_items["Case"] = item_codes[int(choice) - 1]
        total_price += prices[int(choice) - 1]
        break
    else:
        print("Invalid input. Please choose 1 or 2.")

# Input and validation for RAM
while True:
    print("Choose RAM:")
    for i in range(2, 5):
        print(f"{i - 1}. {descriptions[i]} - ${prices[i]:.2f}")

    choice = input("Enter the number of your choice (1/2/3): ")
    if choice in ["1", "2", "3"]:
        selected_items["RAM"] = item_codes[int(choice) + 1]
        total_price += prices[int(choice) + 1]
        break
    else:
        print("Invalid input. Please choose 1, 2, or 3.")

# Input and validation for Main HDD
while True:
    print("Choose Main Hard Disk Drive:")
    for i in range(5, 8):
        print(f"{i - 4}. {descriptions[i]} - ${prices[i]:.2f}")

    choice = input("Enter the number of your choice (1/2/3): ")
    if choice in ["1", "2", "3"]:
        selected_items["Main HDD"] = item_codes[int(choice) + 4]
        total_price += prices[int(choice) + 4]
        break
    else:
        print("Invalid input. Please choose 1, 2, or 3.")

# Output selected items and total price
print("Selected items:")
for key, value in selected_items.items():
    print(f"{descriptions[item_codes.index(value)]}: ${prices[item_codes.index(value)]:.2f}")
print(f"Total Price: ${total_price:.2f}")
