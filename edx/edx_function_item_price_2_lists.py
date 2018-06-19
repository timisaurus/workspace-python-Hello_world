# A function that accepts 2 lists as parameters and returns the total price.
def items_price(a, b):
    counter_a = 0
    counter_b = 0
    price_output = 0
    for items in range(len(a)):
        price_output += (a[counter_a] * b[counter_b])
        counter_a += 1
        counter_b += 1
    return price_output
