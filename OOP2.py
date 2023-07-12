'''
Below are the propteries/attributes of class girl 
classes are defined.
all objects under this class must fulfil the attributes of the class.
We use the dot(.)operator to access the value of a property in a class. (print(Girl.name))
There are things that real world objects do to themselves or others which is called a 'METHOD'.
In a method you find behaviours which determine how you impact others.
The lines of code within a function written in structured programming are called 'behaviours'in OOP
what is defined as a 'function' in structured programming is called 'METHOD' in OOP
When printing a method of a value, there should be a 'return' statement.
all objects of a class will have the same exact METHOD.
we have static and dynamic classes.
'''








class Girl: #this is a static class
    name = 'Martha'
    age = 20
    gender = 'female'
    size = 'petite'
    family = 'kalumba'
    size_of_bra = 'big'
    def greet(): #this is a METHOD.
        print('WELCOME WORLD') #this is the behaviour
        print('Hello World!')
        return '' #always have a return statement in a method.
    def dance():
        print('maganda')
        return ''
    def shower():
        print('showers twice')
        return ''
Girl.greet()
Girl.dance()
Girl.shower()

        
print(Girl.age)

girl2 = Girl()
girl2.name = 'Claire'
girl2.age = 30
girl2.gender = 'female'
print(girl2.name)

girl3 = Girl()
girl3.name = 'Grace'
girl3.age = 25
girl3.gender = 'female'
print(f"{girl3.name} is {girl3.age} years old")

#assignment: create 10 classes with coresponding 5 objects.

