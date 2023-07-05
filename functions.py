#functions to create two values
# a group of statements is called a function
#num1 = 50
#num2 = 100
#num3 = num1 + num2
#print(num3)

def sum():      #this is a function definition.
    num1, num2 = 45,60
    num3 = num1+num2
    print(num3)
sum()    #this is a function call or invocation.

def sub():  
    num1, num2 = 50,30
    num3 = num1-num2
    print(num3)
    
sub()    

def rem():
    num1, num2 =10,3
    num3 = num1%num2
    print(num3)
    
rem()    

def div():
    num1, num2 = 10,5
    num3 = num1/num2
    print(num3)
    
div()    

def myList():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    print(list1[6])
    
myList()    

# the above are called static parameters. e.g ()