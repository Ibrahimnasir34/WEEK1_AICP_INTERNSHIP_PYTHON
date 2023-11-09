# Function to apply discounts and calculate the final price
def apply_discount(total_price, additional_items):
    discount = 0.0
    if len(additional_items) == 1:
        discount = total_price * 0.05
    elif len(additional_items) >= 2:
        discount = total_price * 0.10
    return total_price - discount, discount

final_price, discount = apply_discount(total_price, additional_items)

# Output the amount saved and the new price
print(f"Amount saved: ${discount:.2f}")
print(f"Final Price after discount: ${final_price:.2f}")
