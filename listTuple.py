#lists,tuple and dictionary in details.
#lists are mutable data types
def my_list1():
    my_list1 = [0,1,2,3,4,5,6,7,8,9]
    print(my_list1[5])
    my_list2 = [10,20,30,40,50]
    print(my_list2[4])
    print(my_list2[-1])
    
my_list1()    

def osman():
    osman = [100,[200]]
    print(osman[1][0])
    osman2 = [1000,[[2000,3000]]]
    print(osman2[1][0][1])
    
osman()

def mutable():
    #example of mutable lists(means you can add and remove data there)
    osman.append(1000)
    print(osman)
    osman.pop()
    print(osman)
    fruits = ["orange","pineapple,"]
    fruits.append("apple")
    print(fruits)
    fruits.pop()
    print(fruits)
    
mutable()    



def mytuples():
    #tuples in details
    #tuples are immutable (meaning cant add nor remove anything)
    mytuples = (10,20,30,40,50)
    
mytuples()    


def mapping():
    #mapping in details
    #dictionary
    #dict is immutable
    zebra = {'name' :'tongs', 'legs' :'4', 'color':'black & white', 'sex':'male'}
    print(zebra.keys())
    print(zebra.values())
    zebra.__delitem__('sex')
    print(zebra)
    
mapping()    