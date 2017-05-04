from Customer import *



def main():
  print("Welcome to Wake-Mart. Please register. ")
  print("\n")
  name = input("Enter your name: ")
  cust = Customer(name)
  cust.inputCardsInfo()
  print("Registration completed")
  totalPrc = scanPrices()
  totalCoup = scanCoupons()
  netAmt = totalPrc - totalCoup
  print("Please pay this amount: ", netAmt)
  print("\n")
  print("\n")
  makePayment(cust,netAmt)
  
  
  
main()
  
