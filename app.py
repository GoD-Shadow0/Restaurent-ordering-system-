menu = {
  "Pizza": 100,
  "Burger": 80,
  "Noodles": 80,
  "Fries": 60,
  "sandwichs": 60,
  "coke":50,
}

def print_menu():
  print("\nMenu:")
  for item, price in menu.items():
      print(f"{item}: Rs{price:.2f}")

def take_order():
  order = {}
  while True:
      print("\nCurrent Order:")
      for item, quantity in order.items():
          print(f"{item}: {quantity} x ₹{menu[item]:.2f} = ₹{menu[item] * quantity:.2f}")
      print("Total: ₹%.2f" % calculate_total(order))

      item = input("\nEnter an item to add (or 'done' to finish ordering): ").strip()
      if item == "done":
          break
      if item in menu:
          quantity = int(input(f"Enter the quantity of {item}: "))
          if item in order:
              order[item] += quantity
          else:
              order[item] = quantity
      else:
          print("Item not found in the menu. Please choose from the menu.")

  return order

def calculate_total(order):
  total = 0
  for item, quantity in order.items():
      total += menu[item] * quantity
  return total

def print_receipt(order, total):
  print("\nReceipt:")
  print("Table Number: %d" %tableno)
  for item, quantity in order.items():
      print(f"{item}: {quantity} x ₹{menu[item]:.2f} = ₹{menu[item] * quantity:.2f}")
  print(f"Total: ₹%.2f" % total)
  print("Thank you for dining with us!")

if __name__ == "__main__":
  print("Welcome to the restaurant!")

  while True:
      Name=input("Enter your Name: ")
      Phone=int(input("Enter your Phone Number: ")) 
      tableno=int(input("Enter your Table Number: "))
      print_menu()
      customer_order = take_order()
      total_bill = calculate_total(customer_order)

      if total_bill > 0:
          print("\nYour Order Summary:")
          for item, quantity in customer_order.items():
              print(f"{item}: {quantity} x ₹{menu[item]:.2f} = ₹{menu[item] * quantity:.2f}")
          print(f"Total: ₹%.2f" % total_bill)

          finalize = input("\nWould you like to finalize your order? (yes/no): ").strip().lower()
          if finalize == "yes":
              print_receipt(customer_order, total_bill)
              break
          else:
              print("Your order has been canceled. Please continue ordering.")
      else:
          print("No items ordered. Have a nice day!")

