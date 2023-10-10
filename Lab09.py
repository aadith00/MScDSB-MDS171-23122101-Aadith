# Create a petstore class where you have the details of pets available and their details.
#The class will have methods:-
#Store a new pet details
#Search for a pet
#Sell a pet
#List all pets

#importing your petstore class, create a petstore mian file, where you will implement a menu driven program for admin who will manage 
#the store and user who will see the pets and buy pets.

class petstore:

    def _init_(self):
        self.pets = {
            'Dogs' : [] ,
            'Cats' : [] ,
        }

    def addpets(self,type,breed,age,price):
        if type == 'Dogs':
            self.pets['Dogs'].append({
                "Breed" : breed,
                "Age" : age,
                "Price" : price
            })
        elif type == 'Cats':
            self.pets['Cats'].append({
                "Breed" : breed,
                "Age" : age,
                "Price" : price
            })
        else:
            print('Please enter a valid type of animal.')

    def listpets(self):
        print(self.pets)

    def search_sell(self,breed,price):
        n = input("Enter the breed: ")
        if breed == n:
            print("Found")
            print("Cost is: " , price)
        else:
            print("Not found")


pet = petstore()
pet.addpets("Dogs","Rot",6,15000)
pet.addpets("Dogs","Pitbull",4,20000)
pet.listpets()
pet.search_sell("Rot",15000)