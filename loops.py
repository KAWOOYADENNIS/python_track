#loops are instructions that inform a computer to repeatedly perform a specfic task.

def my_count():
    for item in range(10):
        print(item)
my_count()        

def example2():
    languages = ['python', 'java script', 'ruby', 'c++', 'c#', 'java']
    for language in languages:
        print(language)
example2()        

def example3(num):
    for number in range(num):
        print(number)
example3(15)        

def my_lang():
    languages = ['python', 'java script', 'ruby', 'c++', 'c#', 'java']
    for language in languages:
        if language == 'python':
            print('you are currently in python class')
my_lang()        

def even(num):
    for number in range(num):
        if number % 2 == 0:
            print(number)
even(10)            

#alter function even to print odd numbers.
def odd(num):
    for number in range(num):
        if number % 2 == 1:
            print(number)
odd(20)           


def power(p):
    my_po = p**2
    if my_po % 2 == 0:
        print('the power is an even number')
    else:
        print('the power is an odd number')
power(6)    

#research about the "while loop"
#research about the "switch case"