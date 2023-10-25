# Create a menu driven program to collect student deatils:
#Name
#Email
#Phone
#(Use dictionaries to store student detail)

#Menu options
#1. Create students
#Search for students
#Print Students


studentdict = {}

n = int(input('Enter number of students: '))
students = {}

def createstudent():
    for i in range(n):
        name = input('Enter student name: ')
        email = input('Enter student emmail: ')
        phone = input('Enter student number: ')

    
