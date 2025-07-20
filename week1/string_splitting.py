# This is a List
email_list = [
    'faiql.adfdfdf@gmail.com',
    'hello.fdfdfdf@yahoo.com',
    'dfdfd.dfdfeeef@gmail.com',
    "faiq.hesmes@marvel.com",
]

# We do a for loop if we want to go over all items in a list
for i in email_list:
    j = i.split('@')[1]
    # this is an if-else statement
    if j == "gmail.com":
        # this is an f-string
        print(f"{i} is a Gmail User.")
    else:
        # this is an f-string
        print(f"{i} is not a Gmail User.")
