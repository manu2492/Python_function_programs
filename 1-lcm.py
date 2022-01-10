## defining a function to calculate LCM  
#def calculate_lcm(x, y):  
#    # selecting the greater number  
#    if x > y:  
#        greater = x  
#    else:  
#        greater = y  
#    while(True):  
#        if((greater % x == 0) and (greater % y == 0)):  
#            lcm = greater 
#            break  
#        greater += 1
#        print(greater)
#    return lcm    
#  
## taking input from users  
#num1 = int(input("Enter first number: "))  
#num2 = int(input("Enter second number: "))  
## printing the result for the users  
#print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2))


#create a 2d list
x = [1, 2, 3]
y = [4, 5]
z = []
def agregar(x, y):
    for i in x:
        z.append(i)
    for i in y:
        z.append(i)
    print(z)

agregar(x, y)


#remove duplicates
test_list = [1, 3, 5, 6, 3, 5, 6, 1]

list = []

def removeduplicate(arr):
    for i in test_list:
        if i not in list:
            list.append(i)

    print(list)

removeduplicate(test_list)

























