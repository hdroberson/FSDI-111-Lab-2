item1 = float(input("What is the price of the first item? "))
item2 = float(input("What is the price of the second item? "))
item3 = float(input("What is the price of the third item? "))

subTotal = item1 + item2 + item3

tax = 0.09 * subTotal

total = subTotal + tax

print("\nSub total: $" + format(subTotal, ",.2f"), "Tax amount: $" + \
    format(tax, ",.2f"), "Total: $" + format(total, ",.2f"), \
        sep = "\n" )

