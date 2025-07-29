# What do Software Engineers/Data Scientists/AI Engineers/Prompt Engineers do?

Here's a ChatGPT summary that clarifies the distinction: https://chatgpt.com/share/687b387b-fdc4-800e-9c7a-dc7e4e7aeec5

# Setting up your environment

### Option 1: Using GitHub Codespaces

We went over GitHub Codespaces very briefly the other day. If you'd like more resources, you can look into [this (optional) guide]( https://docs.github.com/en/codespaces/quickstart).

### Option 2: Using VS Code (working locally)

1. Install VS Code from https://code.visualstudio.com/
2. Install Python from https://www.python.org/downloads/

# Tutorials This Week

Please watch/code along with this [tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7) from [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g).
Aim to cover videos 2 - 8 in the series. These will you cover basic Python.

- [Strings](https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=2&t=447s&pp=iAQB0gcJCcwJAYcqIYzv)
- [Integers & Floats](https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=3&pp=iAQB)
- [Lists, Tuples & Sets](https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=4&pp=iAQB)
- [Dictionaries](https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=5&pp=iAQB0gcJCcwJAYcqIYzv)
- [Conditionals & Booleans](https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=6&pp=iAQB)
- [Loops & Iterations](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=7&pp=iAQB)
- [Functions](https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=8&pp=iAQB)

# Problem Set

Feel free to ask ChatGPT. But make sure you understand things thoroughly!

### Problem Set 1: Divisors

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

### Problem Set 2: List Less Than Ten

Take a list, say for example this one:  
> a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  
and write a program that prints out all the elements of the list that are less than 5.

Extras:
- Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
- Write this in one line of Python.
- Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

### Problem Set 3: List Remove Duplicates (Functions & Sets)

Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:
- This will require you to learn [lesson 8](https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=8).
- To solve this, you can write two different functions to do this - one using a loop and constructing a list, and another using sets.

# List of Shortcuts

### On your keyboard

> `CTRL + X`: Cut    
> `CTRL + C`: Copy
> `CTRL + C`: In the terminal, it's used to do a Keyboard Interrupt (useful to get out of While loops!)  
> `CTRL + V`: Paste  
> `CTRL + Z`: Undo  
> `CTRL + Y`: Reverses Undo (`CTRL + Z`)   
> `CTRL + D`: In VSCode, this selects the word at the cursor, or the next occurrence of the current selection.
> `CTRL + /`: Comments highlighted code

### In the terminal
> ⬆️: The up button helps you scroll through your previous commands in the terminal
> `TAB`: This helps you do auto complete for file paths

# If you ever find errors
Copy and paste the error into Google. If you recall in our tutorial, we got this error:

> ValueError: invalid literal for int() with base 10

The first thing we got by pasting this into Google was this StackOverFlow link:
https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10

Someone else has probably experienced this error before you so your best friends are ChatGPT & [StackOverFlow](https://en.wikipedia.org/wiki/Stack_Overflow#:~:text=Stack%20Overflow%20serves%20as%20a,fashion%20similar%20to%20a%20wiki.) Good luck!
