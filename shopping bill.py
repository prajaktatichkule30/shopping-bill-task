# Name: Prajakta Tichkule
# Program: Shopping Bill
# Task: 01
# Language: Python

print("Welcome to Shopping Bill System")
print("--------------------------------")

# Calculate electronics amount with 18% GST
def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    total = amount + gst
    return total
# Calculate fashion amount with 13% GST
def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    total = amount + gst
    return total
# Calculate food amount with 7% GST
def calculateFoodGST(e):
    gst = e * 7 / 100
    total = e + gst
    return total
# Calculate total bill after GST
def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    total = electronics + fashion + food
    return total
# Calculate discount and final bill
def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)

    discount = total * 20 / 100
    final_amount = total - discount

    print("\n----------- Shopping Bill -----------")
    print("Total after GST       :", format(total, ".2f"))
    print("Discount (20%)        :", format(discount, ".2f"))
    print("Final payable amount  :", format(final_amount, ".2f"))
    print("------------------------------------")
    print("Thank you for shopping!")

    return final_amount
# Sample values
a = 100
b = 100
c = 100
d = 100
e = 100

# Call the main calculation function
calculateDiscountedBill(a, b, c, d, e)