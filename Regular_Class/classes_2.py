class car:

    def __init__(self , manu, mod , yr) -> None:
        self.Manufacturer = manu
        self.Model = mod
        self.Year = yr

    def __str__(self) -> str:                  # Used to convert object to string
        return self.Manufacturer

bmw = car('BMW' , '5 series' , 2020)
print(bmw.Manufacturer)

ferrari = car('Ferrari' , 'A Series' , 2023)
print(ferrari.Year)

name = input('Enter car name: ')
audi = car(name , 'dfgh' , 2019)
print(audi.Manufacturer)