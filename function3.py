def add(num1,num2):
    num3 =num1 +num2
    print(num3)
    
def sub(num1,num2):
    num3 = num1 - num2
    print(num3)
        
#forcing the functions to communicate

def add2(num1,num2): #num1 and num2 are parameters
    num3 = num1 + num2
    return num3

def sub2(num1):
    num3 = add2(7,10) - num1
    print(num3)
    
sub2(5)  # 5 is an argument or actual parameter or formal parameters.    

#the above functions are called dynamic or paremeterized functions. 
#the values we give during a function call are called arguments     