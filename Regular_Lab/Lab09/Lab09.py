# Create a petstore class where you have the details of pets available and their details.
# The class will have methods:-
# Store a new pet details
# Search for a pet
# Sell a pet
# List all pets

# importing your petstore class, create a petstore mian file, where you will implement a menu driven program for admin who will manage 
# the store and user who will see the pets and buy pets.

class petstore:

    def _init_(self):
        self.pets = {
            "Dogs" : [
                {"Breed" : "German Shepherd" , "Age" : 1 , "Price" :  6000}, {"Breed" : "Lab" , "Age" : 2 , "Price" : 5000}
                ] ,

            "Cats" : [
                {"Breed" : "xyz" , "Age" : 1 , "Price" : 2000}
            ] 
        }

    def addDetails(self,type,breed,age,price):
        if type == "Dogs":
            self.pets["Dogs"].append({"Breed" : breed, "Age" : age, "Price" : price})
        elif type == 'Cats':
            self.pets["Cats"].append({"Breed" : breed, "Age" : age, "Price" : price})
        else:
            print('Please enter a valid category of animal.')

    def listpets(self):
        print(self.pets)

    def search(self,name):
        n = input("Enter the breed: ")
        if name == n:
            print("Found")
        else:
            print("Not found")

pet = petstore()
pet.addDetails("Dogs","German",2,10000)