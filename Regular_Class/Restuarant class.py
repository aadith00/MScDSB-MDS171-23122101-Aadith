# Create a class restuarant that accepts item name and quantity as input
# inside your class you are giving the item and its cost (per unit price) as a dictionary
# create a function to calculate total cost that prints the item names qty and total cost


class restuarant:

    def __init__(self , item_name , qty) :

        self.item = item_name
        self.quant = qty
        self.menuitems = {

            'RICE' : 30 ,
            'CHICKEN' : 120 ,
            'DAL' : 60 ,
            'CHAPATHI' : 10
            
        }

    def totalcost(self):

        print('Total cost of the order')
        print('Item: \t' , self.item)
        print('Quantity: \t' , self.quant)
        total = self.quant * self.menuitems[self.item]
        print('Total: \t' , total)

order = restuarant('CHICKEN' , 4)
order.totalcost()