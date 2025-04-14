#Step 1: Build the ItemToPurchase class
#Class definition
class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0.00, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
#Method
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_price * self.item_quantity:.2f}")

#Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.
def main():
    #Create item objects
    itemOne = ItemToPurchase()
    itemTwo = ItemToPurchase()
    #Create a list containing the objects
    itemList = [itemOne, itemTwo]
    #Control variable for loop
    i = 1
    #Loop to obtain user input
    for item in itemList:
        print('Item ' + str(i))
        item.item_name = input("Enter item name: ")
        item.item_price = float(input("Enter item price: "))
        item.item_quantity = int(input("Enter item quantity: "))
        i += 1

#Step 3: Add the costs of the two items together and output the total cost
    print('\nTOTAL COST')
    #Create variable for total cost
    total = 0
    #Run through item list to print details and aggregate total
    for item in itemList:
        item.print_item_cost()
        total += item.item_price * item.item_quantity

    print(f'Total = ${total:.2f}')
main()