# Task 01: Shopping Bill — GST First, Discount After

def calculateElectronicsGST(a, b):
    total = a + b
    return total + (total * 0.18)

def calculateFashionGST(c, d):
    total = c + d
    return total + (total * 0.13)

def calculateFoodGST(e):
    return e + (e * 0.07)

def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)
    return electronics + fashion + food

def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 0.20
    final_amount = total - discount
    return final_amount

# Main execution (Sample Test Values: a = 100, b = 100, c = 100, d = 100, e = 100)
if __name__ == "__main__":
    a = 100
    b = 100
    c = 100
    d = 100
    e = 100

    # कॅल्क्युलेशन
    total = totalBill(a, b, c, d, e)
    discount = total * 0.20
    final_payable = calculateDiscountedBill(a, b, c, d, e)

    # एक्सपेक्टेड आउटपुट फॉरमॅट
    print(f"Total after GST = ₹{total:.2f} | Discount = ₹{discount:.2f} | Final payable amount = ₹{final_payable:.2f}")