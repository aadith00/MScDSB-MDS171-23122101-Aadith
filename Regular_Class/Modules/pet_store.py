# Create a petstore class where you have the details of pets available and their details.
#The class will have methods:-
#Store a new pet details
#Search for a pet
#Sell a pet
#List all pets

#importing your petstore class, create a petstore mian file, where you will implement a menu driven program for admin who will manage 
#the store and user who will see the pets and buy pets.

class petstore:

    def __init__(self):
        file = open('Petstore.txt' , '+a')
        file.close()
        self.store = file

    def storeDetails(self,category,name,age):
        self.category = category
        self.name = name
        self.age = age
        self.store = open('Petstore.txt' , '+a')
        self.store.write('Category \t' + 'Name \t' + 'Age \t' '\n')
        self.store.write(category + '\t' + name + '\t' + age)
        self.store.close()

        
# pet = petstore()
# pet.storeDetails('Dog','Pluto','3')