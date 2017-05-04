class Customer(object):
  def __init__(self,name):
    self.name = name
    self.creditCard = 0
    self.debitCard = 0
  
  def inputCardsInfo(self):
      self.ccard = str(input("Enter credit card number: "))
      self.ccardno = self.ccard.replace("-","")
      self.lastcFour = self.ccard[-4:]
      self.ccardno = int(self.ccardno)
      self.security_code = int(input("Enter 3-digit security code: "))
      self.dcard = str(input("Enter debit card number: "))
      self.dcardno = self.dcard.replace("-","")
      self.lastdFour = self.dcard[-4:]
      self.dcardno = int(self.dcardno)
      self.pin = int(input("Enter 4-digit PIN: "))
  
  def verifyCreditCard(self, security_code):
      if len(str(security_code)) == 3 and security_code == self.security_code:
          return True
      return False
        
  def verifyDebitCard(self, pin):
      if len(str(pin)) == 4 and pin == self.pin:
          return True
      return False


def readCouponList():
  coupons = {}
  file = open("coupon_list.txt","r")
  for line in file:
      coupon = line.split(" ")
      coupons[int(coupon[0])] = float(coupon[1])
  file.close()
  return coupons

def readPriceList():
  prices = {}
  file = open("price_list.txt","r")
  for line in file:
    price = line.split(" ")
    prices[int(price[0])] = float(price[1])
  file.close()
  return prices

def scanPrices():
  prices = readPriceList()
  print("Price list: ")
  for code, price in prices.items():
    print(code, price)
  userList = {}
  totalPrc = 0
  while True:
    code = int(input("Enter the price code: " ))
    if code == 9999:
      break
    else:
      fg = 0
      for cde, prc in prices.items():
        if cde == code:
          print("Item found price = ", prc)
          userList[cde] = prc
          totalPrc += prc
          fg = 1
          break
      if fg == 0:
        print("Item not found. ")
  print("User ordered items: ")
  for code, price in userList.items():
    print(code, price)
  print("Total price: ", totalPrc)
  return totalPrc
  
  
def scanCoupons():
  coupons = readCouponList()
  print("Coupons List")
  for code, price in coupons.items():
    print(code, price)
  userList = {}
  totalPrc = 0
  while True:
    code = int(input("Enter 4-digit coupon code: "))
    if code == 9999:
      break
    else:
      fg = 0
      for line, prc in coupons.items():
        if line == code:
          print("Coupon found. Value: ", prc)
          userList[line] = prc
          totalPrc += prc
          fg = 1
          
      if fg == 0:
        print("Coupon not found")
      print("Coupons used: ")
      for code, price in userList.items():
        print(code, price)
      print("Total coupon value:  ", totalPrc)
      return totalPrc
      
      
def makePayment(cust, amount):
  paySucc = 0
  while paySucc != 1:
    payMode = int(input("Select the payment method. 1 for credit. 2 for debit. "))
    if payMode == 1:
      security_code = int(input("Enter security code: "))
      fg = cust.verifyCreditCard(security_code)
      if fg == False:
        paySucc = 0
        print("Security code incorrect. Payment rejected.")
      else:
        paySucc = 1
        print("The amount of ", amount, " will be charged to card number ending with ", cust.lastcFour)
    elif payMode == 2:
      pin = int(input("Enter PIN: "))
      fg = cust.verifyDebitCard(pin)
      if fg == False:
        paySucc = 0
        print("PIN Incorrect. Payment rejected.")
      else:
        paySucc = 1
        print("The amount of ", amount, " will be charged to card number ending with ", cust.lastdFour)
