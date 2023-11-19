def calculate_volume(size, quantity):
    if size == "bucket":
        volume = (10 / 1000) * quantity
    elif size == "trash bag":
        volume = (27 / 1000) * quantity
    elif size == "wheelbarrow":
        volume = (80 / 1000) * quantity
    else:
        print("Invalid size")
        return None
    return volume

def calculate_price(volume, package):
    base_price = volume * 0.05
    if package == "pickup":
        return base_price
    elif package == "cleaning & pickup":
        return 1.2 * base_price
    else:
        print("Invalid package")
        return None

def bid(bidding_price, calculated_price):
    if bidding_price < calculated_price:
        print("Status: Rejected")
        print("Price too low.")
        return 0
    else:
        print("Status: Approved")
        print("Price:", calculated_price)
        return 1

# Main program
print("Select a package (pickup / cleaning & pickup)")
package = input("Enter package type: ")
print("Select a trash size")
size = input("Enter trash size (bucket / trash bag / wheelbarrow): ")
print("Select the trash quantity")
quantity = int(input("Enter trash quantity: "))

if quantity > 0:
    if quantity > 1:
        volume = calculate_volume(size, quantity)
        if volume is not None:
            print(f'The volume is {volume} and the size is {size}')
            price_1 = calculate_price(volume, package)
    else:
        volume = size / 1000
        if volume is not None:
            price = calculate_price(volume, "pickup")
else:
    print("Set a trash quantity of at least one")

bidding_price = float(input("Enter bidding price: "))
bid_status = bid(bidding_price, price_1 if quantity > 1 else price) if quantity > 0 else 0

