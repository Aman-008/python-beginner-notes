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