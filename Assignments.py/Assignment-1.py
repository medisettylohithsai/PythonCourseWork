# ===== Magicpin App =====



# Customer ID
cust_id = int(input("Enter customer id: "))     #456321

# Item Name
name_of_item = input("Enter which item you want: ")   #chicken dum briyani,chicken fry briyani....etc

# Cost
cost_of_item = float(input("Enter the cost of item: "))  #100.98

# Categories (list)
categories = input("Enter categories: ").split(",") #chicken fry,chicken dum,chicken juicy

# Stock Details (tuple)
available_stock = int(input("Enter available stock: "))
sold_items = int(input("Enter sold items: "))
stock_details = (available_stock, sold_items)   #10,8

# Discount
Discount = float(input("Enter discount percentage: ")) #25.5%

# Unique Features (set)
unique_features = set(input("Enter unique features: ").split(",")) #Spicy,Hot,Fresh,Spicy


# customer Details (dictionary)
supplier_name = input("Enter supplier name: ")   #Krishna
supplier_contact = input("Enter supplier contact number: ")   #70214569873
supplier_location = input("Enter supplier location: ")        #HYD

customer_detailes = {
    "Name": supplier_name,
    "Contact": supplier_contact,
    "Location": supplier_location
}



# ===== Display Using Different Formatting Methods =====

# 1. Comma Separation
print("Comma Separation Output:")
print(cust_id, name_of_item, cost_of_item, categories,
      stock_details, Discount, unique_features, customer_detailes, sep=", ")
print()

# 2. Percentage (%) Formatting
print("Percentage Formatting Output:")
print("Customer ID: %d" % cust_id)
print("Item Name: %s" % name_of_item)
print("Cost: ₹%.2f" % cost_of_item)
print("Discount: %.1f%%" % Discount)
print()

# 3. f-Strings
print("f-string Output:")
print(f"Customer ID: {cust_id}")
print(f"Item Name: {name_of_item}")
print(f"Cost: ₹{cost_of_item}")
print(f"Categories: {categories}")
print(f"Stock Details (Available, Sold): {stock_details}")
print(f"Discount: {Discount}%")
print(f"Unique Features: {unique_features}")
print(f"Supplier Details: {customer_detailes}")
print()

# 4. .format() Method
print(".format() Method Output:")
print("Customer ID: {}".format(cust_id))
print("Item Name: {}".format(name_of_item))
print("Cost: ₹{}".format(cost_of_item))
print("Categories: {}".format(categories))
print("Stock Details: {}".format(stock_details))
print("Discount: {}%".format(Discount))
print("Unique Features: {}".format(unique_features))
print("Supplier Details: {}".format(customer_detailes))
