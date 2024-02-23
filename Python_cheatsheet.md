# Python Cheatsheet

CCC - Python Programming

## Cmd/Terminals

Command (Windows) |	Command (MacOS / Linux) |	Description	| Example
| -------- | ------- | ------- | ------- |
exit |	exit	| close the window	| exit
cd	| cd	| change directory	| cd test
cd	| pwd	| show the current directory	| cd (Windows) or pwd (MacOS / Linux)
dir	| ls	| list directories/files | dir
copy	| cp	| copy file	| copy c:\test\test.txt c:\windows\test.txt
move	| mv	| move file	| move c:\test\test.txt c:\windows\test.txt
mkdir	| mkdir	| create a new directory	| mkdir testdirectory
rmdir (or del)	| rm	| delete a file	| del c:\test\test.txt
rmdir /S	| rm -r	| delete a directory	| rm -r testdirectory
[CMD] /?	| man [CMD]	| get help for a command	| cd /? (Windows) or man cd (MacOS / Linux)

Link: [Cmd/Terminal Reference](https://ss64.com/)

## Syntax
The `print()` function is used to display or print output.

```
>>> print("Hello World")
Hello World
```

## Indentation in Python
Indentation means leaving a `TAB` space from margin and in Python it is used to show that statements which are indented belong to the upper statement.

## Comment
Single Line Comments
```py
salary = salary * 1.02   # increase salary by 2%
```
Multi-Line Comments
```py
def increase(salary, percentage, rating):
    """ increase salary base on rating and percentage
    rating 1 - 2 no increase
    rating 3 - 4 increase 5%
    rating 4 - 6 increase 10%
    """
```

## Variables 

Variables are containers that are used to store values.

**Rules for defining a variable in Python**

- Variable name can contain alphabets, digits, and underscore `_`. E.g., `total_amount_1 = 65.85`
- Variable name van start with an alphabet and underscore only. E.g., `college_name = "CCC"`
- It's can't start with a digit. (It should start with a lower case letter).
- No whitespace and reserved keywords are allowed to be used as a variable name.
- Variables are case-sensitive.

## Data Types

Variables can store data of different types, and different types can do different things.

Type |	Examples |
| :-------- | :------- | 
Strings |	`message = "Hello world!"`	|
Number: integer	| `count = 10`	|
NUmber: float | `percentage = 0.8` |
Boolean | `isActive = True` `isAdmin = False` |
List | `lottery = [3, 42, 12, 19, 30, 59]` |
Dictionary | `student = {'name': 'Jason', 'city': 'Richmond', 'test_result': [60, 75, 90, 88]}`| 


## Casting / Type Convertion

Casting is done when you want to specify a type on a variable.
- `int(x)`: convert an integer number from an integer, float and string.
- `float()` - convert a float number from an integer literal, a float literal or a string.
- `str()` - convert a string from a wide variety of data types, including strings, integer and float.

Casting Examples | 
| :-------- |
`y = int(2.8)` y will be 2 |
`z = int("3")` z will be 3 |
`x = float(1)` x will be 1.0|
`z = float("3")` z will be 3.0|
`y = str(2)` y will be '2' | 
`z = str(3.0)` z will be '3.0'|

## Arthmetic Operators

Operator | Name | Example
:-------- | :-------- | :--------
`+`	| Addition	| `x + y`	
`-`	| Subtraction	| `x - y`
`*`	| Multiplication | `x * y`	
`/`	| Division |	`x / y	`
`%`	| Modulus	 | `x % y`	
`**`|	Exponentiation | `x ** y`

## Assignment Operators

Operator | Example | Same as
:-------- | :-------- | :--------
`=`	  | `x = 5`   | `x = 5`	
`+=`	| `x += 3`	| `x = x + 3`	
`-=`  |	`x -= 3`	| `x = x - 3`	
`*=`  |	`x *= 3`	| `x = x * 3`	
`/=`  |	`x /= 3`	| `x = x / 3`	
`%=`  |	`x %= 3`	| `x = x % 3`	
`//=` |	`x //= 3`	| `x = x // 3`	
`**=` |	`x **= 3`	| `x = x ** 3`

## Comparison Operator

- `x == y` means: x is equal to y
- `x != y` means: x is not equal to y
- `x > y` means: x is greater than y
- `x < y` means: x is less than y
- `x <= y` means: x is less than or equal to y
- `x >= y` means: x is greater than or equal to y

## Logical Operator

Logical operator are used to combine conditional statements
- `and`: If you use the `and` operator, both comparisons have to be `True` in order for the whole command to be `True`
- `or`: If you use the `or` operator, only one of the comparisons has to be `True` in order for the whole command to be `True`
- `not`: Reverse the result, returns `False` if the result is `True`

## Input Method
The `input()` function is used to take input as string or character from the user as follows:
```py
name = input("Enter your name: ")
print("My name is: ", name)
```
To take input as an integer:
```py
number = input("Enter the integer value: ")
print("The number is ", number)
```

## Conditional Statement

**if Statement**
```py
if (conditional expression):
  statements
```

**if-else Statement**
```py
if (conditional expression):
  statements
else:
  statements
```

**if-elif Statement**
```py
if (conditional expression):
  statements
elif (conditional expression):
  statements
else:
  statements
```

**Nested if-else Statement**
```py
if (conditional expression):
  if (conditional expression):
    statements
  else:
    statements
else:
  statements
```

## Loops

A loop or iteration statement repeatedly executes a statement, known as the loop body, until the controlling expression is false.

**For Loop**
```py
names = ['Jason', 'John', 'Michael', 'Rachel', 'Admin']
n = len(names)

for i in range(n):
  print(f"Hello {names[i]}")

for name in names:
  hi(name)
```

**While Loop**
```py
i = 0
while i < n:
  print(f"Hello {names[i]}")
  i += 1
```
- The `break` is used for terminating a for a loop prematurely regardless of the results of the conditional tests.
- The `continue` statement is used for skipping the current iteration and starts the next one in a loop.

A function is a reusable block of code that performs a specific task. You can pass parameters into a function. It help to make code organized and manageable.

## Functions

**Function definition**
```py
def my_function():
  statement
```
**Function call**
```py
my_function()
```

## Classes

```py
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    return f"Hi, it's {self.name}."
  
  def __str__(self):
    return f"{self.name} is {self.age} years old."

person = Person('John', 25)
print(person.name)
print(person.age)
print(person)
```

## Static Methods

```py
class TemperatureConverter:
  @staticmethod
  def celsius_to_fahrenheit(c):
    return 9 * c / 5 + 32

  @staticmethod
  def fahrenheit_to_celsius(f):
    return 5 * (f - 32) / 9
```

## Class Inheritance

```py
class Employee(Person):
  def __init__(self, name, age, job_title):
    super().__init__(name, age)
    self.job_title = job_title
  
  def greet(self):
    return super().greet() + f" I'm a {self.job_title}."
```

## String

```py
my_var = "Welcome to Chili's"
my_var.title() # => 'Welcome To Chili's'
my_var.lower() # => 'welcome to chili's'
my_var.upper() # => 'WELCOME TO CHILI'S'

text = "Silicon Valley"
text.split()  # => ['Silicon', 'Valley']
text.split('i') # => ['S', 'l', 'con Valley']

text1 = '   apples and oranges   '
text1.strip() # => 'apples and oranges'

mountain_name = "Mount Kilimanjaro"
print(mountain_name.find("o")) # Prints 1 in the console.

fruit = "Strawberry"
fruit.replace('r', 'R') # => 'StRawbeRRy'

x = "-".join(["hello", "world", "python"]) # => 'hello-world-python'

game = "Popular Nintendo Game: Mario Kart"
print("l" in game) # => True
print("x" in game) # => False

str = 'yellow'
str[1]     # => 'e'
str[-1]    # => 'w'
str[4:6]   # => 'ow'
str[:4]    # => 'yell'
str[-3:]   # => 'low'
```

# List

```py
# Adding List Together
items = ['cake', 'cookie', 'bread']
total_items = items + ['biscuit', 'tart'] # => ['cake', 'cookie', 'bread', 'biscuit', 'tart']

# Lists Data Types
numbers = [1, 2, 3, 4, 10]
names = ['Jenny', 'Sam', 'Alexis']
mixed = ['Jenny', 1, 2]
list_of_lists = [['a', 1], ['b', 2]]

# Append values
orders = ['daisies', 'periwinkle']
orders.append('tulips')
orders # => ['daisies', 'periwinkle', 'tulips']

# Index
berries = ["blueberry", "cranberry", "raspberry"]
berries[0]   # "blueberry"
berries[2]   # "raspberry"

# A 2D-list of names and hobbies
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies) # => [["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

# Remove a element
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
shopping_line.remove("Chris")
print(shopping_line) # => ["Cole", "Kip", "Sylvana", "Chris"]

# Count
backpack = ['pencil', 'pen', 'notebook', 'textbook', 'pen', 'highlighter', 'pen']
numPen = backpack.count('pen')
print(numPen) # => 3

# Length of List
knapsack = [2, 4, 3, 7, 10]
size = len(knapsack) # => 5

# Sort
exampleList = [4, 2, 1, 3]
exampleList.sort() # => [1, 2, 3, 4]

# Slicing
tools = ['pen', 'hammer', 'lever']
tools_slice = tools[1:3] # => ['hammer', 'lever']
tools_slice[0] = 'nail'
# Original list is unaltered:
print(tools) # => ['pen', 'hammer', 'lever']

# Pop
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
removed_element = cs_topics.pop()
print(cs_topics) # => ['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
print(removed_element) # => 'Clowns 101'
cs_topics.pop(2) # Pop the element "Baloon Making"
print(cs_topics) # => ['Python', 'Data Structures', 'Algorithms']
```

# Dictionary

```py
# Create a dictionary
student = {'name': 'Jason', 'city': 'Richmond', 'test_result': [60, 75, 90, 88]}

# Number of key-value pairs
len(student) # => 3

# Add a new key-value pair
student['favorite_language'] = 'Python'

# Pop/Remove a pair
student.pop('favorite_language') # => 'Python'

# Update existing pair
student['city'] = 'Burnaby'

# Merging dictionaries
dict1 = {'color': 'blue', 'shape': 'circle'}
dict2 = {'color': 'red', 'number': 42}
dict1.update(dict2) # dict1 is now {'color': 'red', 'shape': 'circle', 'number': 42}

# Dictionary value types
dictionary = {
  1: 'hello', 
  'two': True, 
  '3': [1, 2, 3], 
  'Four': {'fun': 'addition'}, 
  5.0: 5.5
}

# Dictionary Key-Value Methods
ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah"}

ex_dict.keys() # => dict_keys(["a","b","c"])
ex_dict.values() # => dict_values(["anteater", "bumblebee", "cheetah"])
ex_dict.items() # => dict_items([("a","anteater"),("b","bumblebee"),("c","cheetah")])
```