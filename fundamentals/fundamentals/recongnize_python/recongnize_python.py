num1 = 42 # variable declaration, initialize Number
num2 = 2.3 # variable declaration, initialize Number
boolean = True # variable declaration, initialize Boolean
string = 'Hello World' # variable declaration, initialize String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# variable declaration, initialize List with Strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# variable declaration, initialize Dictionary with key nad values of strings/numbers/boolean
fruit = ('blueberry', 'strawberry', 'banana')
# variable declaration, initialize Tuples with strings
print(type(fruit)) # log statement tuple value
print(pizza_toppings[1]) # log statement list value of index 1
pizza_toppings.append('Mushrooms') # add value into the last index of list
print(person['name']) # log statement dictionary value thru the key
person['name'] = 'George' # change the dictionary value string thru key
person['eye_color'] = 'blue' # change the dictionary value string thru key
print(fruit[2]) #log statement tuple value of index of 2

if num1 > 45: # access the num 1 set condition if
    print("It's greater") # log statement the string
else: # else
    print("It's lower") # log statement the string

if len(string) < 5: # access the len of string set condition if length check
    print("It's a short word!") #log statement the string
elif len(string) > 15: # else if another condition in the same statement length check
    print("It's a long word!") #log statement another string
else:   #else
    print("Just right!") #log statement another string

for x in range(5): # for loop start from 0 stop before 5 increment by 1
    print(x) # log statement the x value from start to end
for x in range(2,5): # for loop start from 2 stop before 5 increment by 1
    print(x) # log statement the x value from start to end
for x in range(2,10,3): # for loop start from 2 stop before 10 increment by 3
    print(x) # log statement the x value from start to end
x = 0 # variable declaration with number while loop start from 0
while(x < 5): # stop at 5
    print(x) # log statement the x value from start to end
    x += 1 #increment by 1

pizza_toppings.pop() # delete the list of last index value
pizza_toppings.pop(1) # delete the list of value of index 1

print(person) # log statement the dictionaray of person
person.pop('eye_color') # delete the value and key "eye_color" from the dictionary
print(person) # log statement the dictionaray of person

for topping in pizza_toppings: # for loop in the list start from index 0
    if topping == 'Pepperoni': # if condition the value is the string
        continue # continue the loop
    print('After 1st if statement') # return the string statement
    if topping == 'Olives': #if condition if value is the string
        break # break the for loop

def print_hello_ten_times(): # function declaration with name
    for num in range(10): # for loop start from 0 end before 10
        print('Hello') # log the statement each time of loop

print_hello_ten_times() # fire the function

def print_hello_x_times(x): #function declaration with parameter x
    for num in range(x): # for loop start from 0 end before giving x
        print('Hello') # log the statement each time of loop

print_hello_x_times(4) #fire the function with argument of 4

def print_hello_x_or_ten_times(x = 10): #function declaration with default value of parameter
    for num in range(x): #for loop start from 0 end before giving x or default value
        print('Hello') #log the statement each time of loop

print_hello_x_or_ten_times() # fire function without argument and using the default value
print_hello_x_or_ten_times(4) # fire function with argument of 4


"""
Bonus section
"""

# print(num3) # NameError: name <variable name> is not defined
# num3 = 72 # need to define the value before the function
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent because the space
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'pop'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'append'
