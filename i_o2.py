def paye(salary,name,age,location,type_of_work):
    rate = 0.3
    if salary >= 300000:
        tax = rate*salary
        net_pay = salary - tax
        print('Dear: ',name)
        print('Your age is: ',age)
        print('Your location is: ',location)
        print('Your type of work: ',type_of_work)
        print('Your Tax Payable Is: ',tax)
        print('And Your Net pay is: ',net_pay)
        print('.....................')
    else:
        print('Dear: ',name)
        print('Your age is: ',age)
        print('Your location is: ',location)
        print('Your type of work: ',type_of_work)
        print('Your salary is none taxable')
    print('thank You')
        

        
    
    
    

print('Your Welcome!')
name = raw_input('please input your name here: ')
age = input('Please insert your age here: ')
location = raw_input('Please fill in your location here: ')
salary = input('Please input your salary here: ') 
type_of_work = raw_input('Please insert your Type of work here: ') 



paye(salary,name,age,location,type_of_work)





def examp():
    my_list = []
    num = input('Please enter your lucky number: ')
    my_list.append(num)
    print(my_list)
    for item in my_list:
        print(item)
    
    
examp()