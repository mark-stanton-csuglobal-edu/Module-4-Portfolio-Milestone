#Step 1: Build the ItemToPurchase class
#Class definition
class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0.00, item_quantity = 0):
        self.item_name = "none"
        self.item_price = float(0.00)
        self.item_quantity = int(0)
        self.total_cost = float(item_price * item_quantity)
#Method
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_price * self.item_quantity:.2f}")

#Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.
def main():
    #Create item objects
    itemOne = ItemToPurchase()
    itemTwo = ItemToPurchase()

    #Prompt user to enter attributes for item 1
    print('Item 1')
    itemOne.item_name = input('Enter the item name: ')
    itemOne.item_price = float(input('Enter the item price: '))
    itemOne.item_quantity = int(input('Enter the item quantity: '))

    #Prompt user to enter attributes for item 2
    print('Item 2')
    itemTwo.item_name = input('Enter the item name: ')
    itemTwo.item_price = float(input('Enter the item price: '))
    itemTwo.item_quantity = int(input('Enter the item quantity: '))

#Step 3: Add the costs of the two items together and output the total cost
    print('\nTOTAL COST')
    itemOne.print_item_cost()
    itemTwo.print_item_cost()

    total = ((itemOne.item_price * itemOne.item_quantity) + (itemTwo.item_price * itemTwo.item_quantity))
    print(f'Total = {total:.2f}')
main()