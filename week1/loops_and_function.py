# this is a list
x = [1, 2, 3, 4, 5]
x[0] = 4
print(x)

for i in x:
    print(i * -1)

for x in [1, 2, 3, 4, 5]:
    print(f'{x+3} apples!')

for x in range(1, 10, 2):
    # iterate from i to n-1, with 2 steps
    # where i = 1, n=10
    print(f'{x} apples!') # 1, 3, 5, 7 ... increments of 2

for x in range(10, 0, -2):
    # iterate from i to n-1, with -2 steps
    print(f'{x} apples!')

i = 10
while i > 5: # while {condition is True}, execute the code under it!
    print(i > 5)
    print(i)
    i -= 1
print("Exit out of while loop")
print(i > 5)
print(i)

# don't uncomment this! Infinte loop!
# while True:
#     print("forever") # exit out of eternal while loop with CTRL + C

# while 6 > 10:
#     print('Hello')

while False:
    print("pempeng")

def square_numbers_up(x: int, y: int,):
    z = x + y
    return z**2

print(square_numbers_up(x=3, y=3))

def clean_name_in_database(first_name: str, middle_name: str, last_name: str):
    clean_name = first_name.upper() + " " + middle_name.upper() + " " + last_name.upper()
    return clean_name

print(clean_name_in_database("wAN","adzhar","Faiq"))