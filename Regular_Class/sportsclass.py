#Create a sportmart class where you will have inventory or shelf of items and order of customers
#Create a csv file which will store your inventory details and order details
#with the help of file handling techs in python read the files and create an object for trinity store and populate
#the inventory items and orders for the trinity store object
#to make sure that you have added all the items in your file use a display method to show your inventory and order history

class sportMart:

    def __init__(self):
        self.inventory = {}
        self.orders = {}

    def createOrder(self,Orderid,Item,Quantity,Price,Total):
        temp = {
            'Orderid' : Orderid ,
            'Item' : Item ,
            'Quantity' : Quantity ,
            'Price' : Price ,
            'Total' : Total
        }

        self.orders[Orderid] = temp

    def addinventory(self,Products,Name,Quantity,Price_per_piece):
        add = {
            'Productid' : Products ,
            'Itemname' : Name ,
            'Quantity' : Quantity ,
            'Price' : Price_per_piece
        }

        self.inventory[Products] = add

    def printInventory(self):
        print(self.inventory)

    def printOrders(self):
        print(self.orders)

    def updateInventory(self):
        Products = input('Enter the product id: ')
        Orderid = input('Enter the order id: ')
        new = int((self.inventory[Products]['Quantity']) - int(self.orders[Orderid]['Quantity']))
        self.inventory.replace(self.inventory[Products]['Quantity'] , new)

trinity = sportMart()
orders = open('Order.csv' , '+r')
orders_header = orders.readline()
orders_orders = orders.readlines()
for item in orders_orders:
    temp = item.strip().split(',')
    trinity.createOrder(temp[0],temp[1],temp[2],temp[3],temp[4])

trinity.printOrders()
trinity.createOrder('XYZ01' , 'Bat' , 12 , )