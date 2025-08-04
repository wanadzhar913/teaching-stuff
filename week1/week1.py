# Recap of types in Python
for i in [1, 2.0, 'hello', None, True]:
    print(f'{i} is a {type(i)}')

# Addition
x = 1 + 1
print(x)

# Subraction
x = 1 - 1
print(x)

# Division
x = 2 / 4
print(x)

# Floor Division (Rounds things down)
x = 7 // 2
print(x) # 3

# Divisions by Zero, returns a ZeroDivisionError
# x = 6 / 0
# print(x)

# Multiplication
x = 3 * 8
print(x)

# Modulo Operations (This returns the Remainder as the output)
x = 8 % 3
print(x) # 2 as 8 divided by 3 leaves 2 as a remainder

##### Float operations in Python (Decimals) #####
# Doing division, multiplication, etc. is similar to Integer operations above

x = 1 + 2.0
print(x) # 3.0
print(type(x)) # Float

x = 3.0 / 7.6
print(x)

##### Type Casting (Data Type Conversion) #####
# One convenient feature in Python, is that you can convert a variable into
# different data types

# Integers to Floats
y = 2 # type integer
x = float(y)
print(type(x)) # Float

# Float to Integer
y = 3.8 # type integer
x = int(y) # this rounds down the float to int
print(x)
print(type(x)) # Integer, 3

# Strings to Floats
k = '2.66'
print(k)
print(type(k))

j = float(k)
print(j)
print(type(j))

##### String Methods in Python #####
y = 'hello'

# How to access parts of the string
# In Python, we start counts from 0. In ":" notation, we start from i and end at j - 1.
print(y[0:2]) # This prints 'he' because it starts at i = 0 and j = 2 - 1
print(y[0:5]) # This prints 'hello' because it starts at i = 0 and j = 5 -1
print(y[2:233434]) # This print 'llo'.

# How to split a string
k = 'faiq.hesmes@gmail.com' 
j = k.split('@') # breaks up string by '@'
print(j)
print(type(j)) # str
print(j[1]) # returns: 'gmail.com'

k = 'faiq.hesmes@gmail.com' 
j = k.split('.') # breaks up string by '.'
print(j)
print(type(j)) # str
print(j[1]) # returns: 'hesmes@gmail'

# How to upper/lower/title case a string
x = 'amsterdam'
y = 'HELLO'

print(x.upper()) # returns: 'AMSTERDAM'
print(y.lower()) # returns: 'hello'
print(y.title()) # returns: 'Hello'

