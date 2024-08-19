# # using print()

# print("Hello World")

# # using type()

# a = 10
# print(type(a))

# b = "Apple"
# print(type(b))

# c = 10.5
# print(type(c))




# 1.First  swap method
# a = 5
# b = 7
# a,b = b,a
# print(a)
# print(b)


# 2. Second swap method
# a = 9
# b = 8
# c = a
# a = b
# b = c
# print(a)
# print(b)
# print(2+2/((2+2)+(2**2)))
# print(-3 - (3*-1))
# print(2 -1*(2))
# print(-1 -1*(-1))

#def to_celsius(x):
    
#    '''Convert Fahrenheit to Celsius'''
#    return (x-32) * 5/9


#to_celsius(75)
'''
name = "Aman"
result = len(name)
print("Hello " + name + ". Your lucky number is :  " + str(result))
'''

# def circle_area(radius):
#     pi = 3.14
#     area = pi * (radius ** 2)
#     print(area)

# circle_area(5)
#Output is 78.5


# print("cat"=="dog")
# print("Yellow" > "Cyan")


#print(2+2*(-1))

'''


# This function rounds a variable number up to the nearest 10x value
def round_up(number):
  x = 10
# The floor division operator will calculate the integer value of
# "number" divided by x: 35 // 10 will return the integer 3.
  whole_number = number // x
# The modulo operator will calculate the remainder value of "number"
# divided by x: 35 % 10 will return the remainder value 5.
  remainder = number % x
# If the remainder is greater than or equal to 5: 
  if remainder >= 5: 
# Return x multiplied by the (whole_number+1) to round up
    return x*(whole_number+1)
# Else, return x multiplied by the whole_number to round down
  return x*whole_number
 
# Calls the function with the parameter value of 35.
print(round_up(35)) # Should print 40


'''

'''

x =   0
while x < 5:
    print("value",x,":")
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

'''

'''

x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1

product = 1
while x < 10:
    product = product * x
    x = x + 1

print(sum, product)
#Ouput 45 1

'''



'''


# This function counts the number of integer factors for a 
# "given_number" variable, passed through the function’s parameters.
# The "count" return value includes the "given_number" itself as a 
# factor (n*1). 
def count_factors(given_number):

    # To include the "given_number" variable as a "factor", initialize
    # the "factor" variable with the value 1 (if the "factor" variable
    # were to start at 2, the "given_number" itself would be excluded). 
    factor = 1
    count = 1

    # This "if" block will run if the "given_number" equals 0.
    if given_number == 0:
        # If True, the return value will be 0 factors. 
        return 0

    # The while loop will run while the "factor" is still less than
    # the "given_number" variable.
    while factor < given_number:
        # This "if" block checks if the "given_number" can be divided by
        # the "factor" variable without leaving a remainder. The modulo
        # operator % is used to test for a remainder.
        if given_number % factor == 0:
            # If True, then the "factor" variable is added to the count of
            # the "given_number"’s integer factors.
            count += 1
        # When exiting the if block, increment the "factor" variable by 1
        # to divide the "given_number" variable by a new "factor" value
        # inside the while loop.
        factor += 1

    # When the interpreter exits either the while loop or the top if
    # block, it will return the value of the "count" variable.
    return count


print(count_factors(0)) # Count value should be 0
print(count_factors(3)) # Should count 2 factors (1x3)
print(count_factors(10)) # Should count 4 factors (1x10, 2x5)
print(count_factors(24)) # Should count 8 factors (1x24, 2x12, 3x8, and 4x6). 

'''


'''

def is_power_of_two(number):
  if number <= 0:
    return False
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  while number % 2 == 0:
    number = number // 2
    # print(type(number))
  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
  if number == 1:
    return True
  return False
  
# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False


'''


for x in range(0,101,10):
  print(x)