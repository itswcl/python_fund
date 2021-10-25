#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# return 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# function number_of_days_in_a_week_silicon_or_triangle_sides no defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# return 5 cuz first of return

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# return 5 cuz first of return

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# print 5 > print 5 and none after

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# print 8 > print 3 and 5 error out after because because no value return from function

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# print 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# print 100 then print return value 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # print 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # print 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# return 7 and 14 and sum both up

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# return value 8

#11
b = 500
print(b) # 500 return the asssigned value
def foobar():
    b = 300
    print(b)
print(b) # 500 return the asssigned value
foobar() # 300 return the assigned value within the function
print(b) # 500 return the assigned value out of function


#12
b = 500
print(b) # 500 return the asssigned value
def foobar():
    b = 300
    print(b)
    return b
print(b) # 500 return the asssigned value
foobar() # 300 print the assigned value within the function
print(b) # 500 print outside of value


#13
b = 500 # 500 return the asssigned value
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b) # 500 return the asssigned value
b=foobar() # 300 print the assigned value within the function and assign value to b
print(b) # 300 value updated from above


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# print out value from foo 1  bar 3 foo 2

#15
def foo():
    print(1) # log 1
    x = bar() # assign value with return from bar()
    print(x) # log x value
    return 10 # return value 10
def bar():
    print(3) # log 3
    return 5 # return value 5
y = foo() # assign new value from foo
print(y) # log 10
# 1 3 5 10