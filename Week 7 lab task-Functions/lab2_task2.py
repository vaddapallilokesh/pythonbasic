def calculate_price(price, tax_rate=18, discount=0):
    final_price = price + (price*tax_rate/100)-discount
    return final_price

print("Case 1:", calculate_price(1000))
print("Case 2:", calculate_price(1000, tax_rate=10))
print("Case 3:", calculate_price(1000, tax_rate=12, discount=50))


'''output-
Case 1: 1180.0
Case 2: 1100.0
Case 3: 1070.0
'''
