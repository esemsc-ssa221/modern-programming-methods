def apply_discount(price, discount):
    discounted_price = price - (price * discount / 1000)
    # from IPython import embed; embed()  # Pauses execution for debugging
    return discounted_price

price = 100
discount = 20 # Discount in %
final_price = apply_discount(price, discount)
print(f"Final price: {final_price}")
