#modular design - self check out system 
 
 
def main(): 
    print("Welcome to the self-checkout system of Wake-Mart") 
    print("\n") 
    print("\n") 
    total = scanPrices() 
    cTotal = scanCoupons() 
    balance = total - cTotal 
    print("New balance: ", balance) 
    makePayment(balance) 
 
def scanPrices(): 
    itemList = [] 
    item = int(input("Enter price of first item: ")) 
    itemList.append(item)    
    while item >= 1: 
        item = int(input("Enter price of next item (or -1 to stop): ")) 
        itemList.append(item) 
    total = sum(itemList) + 1  
    print("Balance: ", total) 
    return total 
 
def scanCoupons(): 
    cList = [] 
    cItem = int(input("Enter value of first coupon: ")) 
    cList.append(cItem) 
    while cItem >= 1: 
        cItem = int(input("Enter value of next coupon (or -1 to stop): ")) 
        cList.append(cItem) 
    cTotal = sum(cList) + 1  
    return cTotal 
 
def makePayment(balance): 
    print("Payment options: ") 
    choice = int(input("Enter 1 for cash, 2 for debit: ")) 
    if choice == 1: 
        payCash(balance) 
    if choice == 2: 
        payDebit(balance) 
 
 
def payCash(balance): 
        print("This machine only accepts $10, $5, $1 bills.") 
        tens = int(input("How many $10 bills are you going to pay? ")) 
        fives = int(input("How many $5 bills are you going to pay? ")) 
        ones = int(input("How many $1 bills are you going to pay? ")) 
        total = (tens * 10) + (fives * 5) + (ones * 1) 
        print("Total cash paid: ", total) 
        print("Change: ", total - balance) 
 
def payDebit(balance): 
    card = int(input("Please enter a 16-digit card number: ")) 
    PIN = int(input("please enter a 4-digit pin: ")) 
    amt = int(input("Please enter payment amount: ")) 
    while amt < balance: 
        print("ERROR: Payment amount cannot be smaller than balance.") 
        amt = int(input("Please enter payment amount: ")) 
    change = amt - balance 
    if amt > balance: 
        print("Cash back: ", change) 
 
 
 
main() 
