def calculate_discount(price, discount_percent):
    try:
        price = float(price)
        discount_percent = float(discount_percent)
    except ValueError:
        return "Invalid input. Please enter numerical values for price and discount percentage."
    if(discount_percent > 20):
        return price *  (1 - (discount_percent /  100))
    else:
        return price
    
original_price = input("Enter the original price of the item: ")
discount_percent = input("Enter the discount percentage: ")

print(calculate_discount(original_price, discount_percent))