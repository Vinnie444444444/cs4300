def calculate_discount(price, discount):
    # calcs the final price after a discounted is entered
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be numeric")
    if not isinstance(discount, (int, float)):
        raise TypeError("Discount must be numeric")
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price - (price * discount / 100)

