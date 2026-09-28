def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)
    print("Items:", items)
    print("Discount:", discount)
    print("Extra Info:", extra)

order_summary("Meera", "Laptop", "Mouse", discount=10,
              delivery_address="Hyderabad", gift_wrap=True)


'''
output-
Customer: Meera
Items: ('Laptop', 'Mouse')
Discount: 10
Extra Info: {'delivery_address': 'Hyderabad', 'gift_wrap': True}
'''
