# In main file
# import script1
# print(script1.sum(1, 3))

# You will need to add code in this module to make teh Point of Sale Application functional.


class PointOfSale:
  def __init__(self):
    self.checkout_total = 0 # This is an example varialbe, remove it or change it as you please.
    self.cart = []
    print("\nInitializing Javi's POS system...")
    
    
  def start(self): # This is the function that should be used to start the application.
    while True:
      print("\n----Menu----")
      print("1: Show shopping cart ")
      print("2: Add Items to the cart ")
      print("3: Display Total")
      print("4: Pay")
      print("5: Exit! ")

      choice = input("choose an option froim 1-5:")


      if choice == "1":
        print("this is in your cart")
        self.cart1()
      elif choice == "2":
        self.add_TC2()
      elif choice == "3":
        pass
      elif choice == "4":
        self.purchased4()
      elif choice == "5":
        print("bye bye!!!")
        break
      else:
        print("invalid choice please try again!")


  def cart1(self):
    pass

  def add_TC2(self):       # adding items to my cart
    thing = input("what do you want to add to your cart?")#Ask the user what they want to add

  def total_price3(self):
    pass
  
  def purchased4(self):
    pass