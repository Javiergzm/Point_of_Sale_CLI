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
    print("1: Show shopping cart ")
    print("2: Add Items to the cart ")
    print("3: Display Total")
    print("4: Pay")
    print("5: Bye, Bye! ")
    while True:
      print("Menu please select an option! ")
      choice = input
      if choice == "1":
        print("self.cart")
      else if choice == "2"