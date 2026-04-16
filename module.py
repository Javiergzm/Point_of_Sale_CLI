# In main file
# import script1
# print(script1.sum(1, 3))

# You will need to add code in this module to make teh Point of Sale Application functional.


class PointOfSale:
  def __init__(self):
    self.checkout_total = 0 # This is an example varialbe, remove it or change it as you please.
    self.cart = []
    menu = "yes"
    
    print("\nInitializing Javi's POS system...")
    
    
  def start(self): # This is the function that should be used to start the application.
    print("\n----Menu----")
    print("1: Show shopping cart ")
    print("2: Add Items to the cart ")
    print("3: Display Total")
    print("4: Pay")
    print("5: Bye, Bye! ")

    choice = input("choose an option:")
    
    for i in self:
      choice = input
      if choice == "1":
        print("this is in your cart")
      elif choice == "2":
        pass
      elif choice == "3":
        pass
      elif choice == "4":
        pass
      elif choice == "5":
        break