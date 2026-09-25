#Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")

price = 0
coffee = input("What type of coffee would you like?").title()
if coffee=="Espresso":
   price = price + 2.50
elif coffee=="Americano":
   price = price + 3
elif coffee=="Latte":
   price = price + 2.50
elif coffee=="Cappuccino":
   price = price + 3.00
elif coffee=="Macchiato":
   price = price + 2.50
elif coffee=="Mocha":
   price = price + 3.50
elif coffee=="Flat White":
   price = price + 2.50


#Complete the code here...
size = input("What size would you like? (Medium / Large / XL): ").title()
if size == "Large":
    price = price + 1.00
elif size == "Xl":
    price = price + 1.50

dining_option = input("Eat in or take away? ").title()
if dining_option == "Take Away":
    price = price + 1.00

donate_option = input("Would you like to donate 100£?").title()
if donate_option == "Yes":
    price = price + 100.00
elif donate_option == "No":
    price = price + -0.00

print("----------------------------")
print("Total Cost: £" + str(price))