def paye(salary,name):
    rate = 0.3
    tax = rate*salary
    net_pay = salary - tax
    print('Dear: ',name)
    print('Your Tax Payable Is: ',tax)
    print('And Your Net pay is: ',net_pay)
    print('.....................')
    
    
    
    

print('Your Welcome!')
name = raw_input('please input your name here: ')
salary = input('Please input your salary here: ')   


paye(salary,name)