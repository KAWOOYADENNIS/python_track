'''
the method __init__(constructor) will help us give the actual value of the object
these values are assigned to the proprties of the class i.e name
self is a reference that denotes/identifies the property/attibutes of the class.
self.name is a property being assigned to value 'name' as arugments to the parameter in line def __init__
the number of properties should be the same as the parameters
The first parameter of the __init__ is a reference to the properties and is not counted as a property. ie. 'self'
Instantiation is the creation of objects in the class.
A method of a class that is named __init__ is called a constructor.
A constructor is used to intialise an instantiated object.
the method 'register' is overloaded because each object uses it differently.
'''


class School: #dynamic class
    def __init__(self,name,motto,location,no_teachers,no_students,no_admins,uneb_no):
        self.name = name 
        self.motto = motto
        self.location = location
        self.no_teachers = no_teachers
        self.no_students = no_students
        self.no_admins = no_admins
        self.uneb_no = uneb_no 
    def register(self): 
        print(f"{self.name} is fully registered with UNEB")
        
school1 = School('KINGS','Strive for excellence','space',50,100,20,'U777111') #calling an object is referde to 'instantiation' in classes.
school1.register()
school2 = School('Hillside','make greatness','Naalya',150,500,20,'U0007')       
school2.register()

class Country:
    def __init__(self,A,B,C):
        self.name = A
        self.city = B
        self.pop = C
country1 = Country('Uganda','Kla','58 million people')
        
        
        
class Continent:
    def __init__(continent,A,B,C):
        continent.name = A
        continent.nu_rivers = B
        continent.nu_lakes = C
continent1 = Continent('Africa',100,200)