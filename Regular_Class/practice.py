# get details of students ,check if reg no already exist if exist replace all the details with a new one
# search using register number and print all the details

class students:

    def __init__(self,name,regno,phone):
        self.name = name
        self.regno = regno
        self.phone = phone

    def addDeatails(self,name,regno,phone):
        Details = {
            'Name' : name ,
            'Register NUmber' : regno ,
            'Phone' : phone
        }
        print(Details)

    def search(self,)
