# Assignment 1
## Exercise 1
1.1 Create a variable called `name`
```
>>> name = "Ka Ying Lesley, Lai"
```
1.2 Print the length of your name
```
>>> name_length = len(name)
>>> print(len(name))
19
```
1.3 Split the `name` and store into two variables named `first_name` and `last_name`
```
>>> first_name, last_name = name.split(',')
```
1.4 Print `first_name` and `last_name`
```
>>> print(first_name)
Ka Ying Lesley
>>> print(last_name)
 Lai
>>>
```

## Exercise 2
**List**

1.1 Create a list called `fruits` and store the following strings in order: `'orange'`,`'banana'`,`blueberry'`,`'apple'`,`'grapefruit'`
```
>>> fruits = ['orange', 'banana', 'blueberry', 'apple', 'grapefruit']
```
1.2 Add a new string `'strawberry'` to the list.
```
>>> fruits.append('strawberry')
```
1.3 Print out the `fruits`
```
>>> print(fruits)
['orange', 'banana', 'blueberry', 'apple', 'grapefruit', 'strawberry']
```
1.4 Sort `fruits` in alphabetical order and print out the result
```
>>> fruits.sort()
>>> print(fruits)
['apple', 'banana', 'blueberry', 'grapefruit', 'orange', 'strawberry']
```
1.5 Create a list called `fruits_reverse` which store the fruits in a reversed order and print the result. You cannot change the order of `fruits`
```
>>> fruits_reverse = fruits.copy()
>>> print(fruits_reverse)
['apple', 'banana', 'blueberry', 'grapefruit', 'orange', 'strawberry']
>>> fruits_reverse.reverse()
>>> print(fruits_reverse)
['strawberry', 'orange', 'grapefruit', 'blueberry', 'banana', 'apple']
>>> print(fruits)
['apple', 'banana', 'blueberry', 'grapefruit', 'orange', 'strawberry']
```

**Dictionary**

2.1 Create an empty dictionary named `inventory`
```
>>> inventory = {}
```
2.2 Store your first name and last name in this inventory under keys of `'first_name'` and `'last_name'`
```
>>> inventory = {'first_name' : 'Ka Ying Lesley', 'last_name' : 'Lai'}
```
2.3 Store a copy of `fruits` list under the key of `'fruits'`
```
>>> fruits = ['apple', 'banana', 'blueberry', 'grapefruit', 'orange', 'strawberry']
>>> inventory = {'first_name' : 'Ka Ying Lesley','last_name' : 'Lai','fruits' : ['apple', 'banana', 'blueberry', 'grapefruit', 'orange', 'strawberry']
}
```
2.4 Store the number of fruits in `fruits` list under the key of `'fruits_count'` 
```
>>> inventory = {'first_name' : 'Ka Ying Lesley','last_name' : 'Lai','fruits' : ['apple', 'banana', 'blueberry', 'grapefruit', 'orange', 'strawberry']
,'fruits_count' : len(fruits)}
```
2.5 Print out the `inventory`
```
>>> print(inventory)
{'first_name': 'Ka Ying Lesley', 'last_name': 'Lai', 'fruits': ['apple', 'banana', 'blueberry', 'grapefruit', 'orange', 'strawberry'], 'fruits_count': 6}
```
2.6 Add your favourite fruit to the `inventory` and update the `fruits_count`. You cannot update the list `fruits`
```
>>> inventory['favourite_fruit'] = 'guava'
>>> inventory['fruits_count'] = 7
>>> print(inventory['fruits'])
['apple', 'banana', 'blueberry', 'grapefruit', 'orange', 'strawberry']
```
2.7 Print out the updated `inventory`
```
>>> print(inventory)
{'first_name': 'Ka Ying Lesley', 'last_name': 'Lai', 'fruits': ['apple', 'banana', 'blueberry', 'grapefruit', 'orange', 'strawberry'], 'fruits_count': 7, 'favourite_fruit': 'guava'}
```
## Exercise 3
Rewrite the following JavaScript code to Python code. You should see different output when `choice` has differen value
```
const choice = "sunny"
let textContent
if (choice === "sunny") {
  textContent = "It is nice and sunny outside today. Wear shorts! Go to the beach, or the park, and get an ice cream."
} else if (choice === "rainy") {
  textContent =
    "Rain is falling outside; take a rain coat and an umbrella, and don't stay out for too long."
} else if (choice === "snowing") {
  textContent =
    "The snow is coming down — it is freezing! Best to stay in with a cup of hot chocolate, or go build a snowman."
} else if (choice === "overcast") {
  textContent =
    "It isn't raining, but the sky is grey and gloomy; it could turn any minute, so take a rain coat just in case."
} else {
  textContent = ""
}
console.log(choice)
console.log(textContent)
```

**Rewrite in Python code :**
```
choice = "snowing"

if choice == "sunny":
    textContent = "It is nice and sunny outside today. Wear shorts! Go to the beach, or the park, and get an ice cream."
elif choice == "rainy":
    textContent = "Rain is falling outside; tkae a rain coat and an umbrella, and don't stay out for too long."
elif choice == "snowing":
    textContent = "The snow is coming down - it is freezing! Best to stay in with a cup of hot chocolate, or go build a snowman."
elif choice == "overcast":
    textContent = "It isn't raining, but the sky is grey and gloomy; it could turn any minute, so take a rain coat just in case."
else:
    textContent = ""

print(choice)
print(textContent)


snowing
The snow is coming down - it is freezing! Best to stay in with a cup of hot chocolate, or go build a snowman.
```
## Exercise 4
Implement a number guessing game using Python. The number range is between 1 to 20, players only have 6 chances to guess the correct number.


**Commands**

```
import random

the_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
#print(f"TEST: the correct number is: {the_number}")


for i in range(1, 7):
    print("Take a guess ")
    guess = int(input())

    if guess > the_number:
        print(guess, "Your guess is too high")
    elif guess < the_number:
        print(guess, "Your guess is too low")
    else:
        break

if guess == the_number:
    print(f"Good job! You guessed my number in {i} guesses!")
else:
    print("Sorry you failed! The number I was thinking was " + str(the_number))
```
**Output 1**
```
I am thinking of a number between 1 and 20.
Take a guess 
10
10 Your guess is too high
Take a guess 
5
5 Your guess is too low
Take a guess 
6
6 Your guess is too low
Take a guess 
7
7 Your guess is too low
Take a guess 
8
Good job! You guessed my number in 5 guesses!

Process finished with exit code 0
```
**Output 2**
```
I am thinking of a number between 1 and 20.
Take a guess 
18
18 Your guess is too high
Take a guess 
17
17 Your guess is too high
Take a guess 
16
16 Your guess is too high
Take a guess 
15
15 Your guess is too high
Take a guess 
13
13 Your guess is too high
Take a guess 
12
12 Your guess is too high
Sorry you failed! The number I was thinking was 4

Process finished with exit code 0
```
## Exercise 5
Create a Python classes based on the scenarios. Below is the 2) bank account scenario.

**Commands**
```
class BankAccount:
    def __init__(self, owner_name, account_number, account_type, account_status, date_opened, account_balance):
        self.owner_name = owner_name
        self.account_number = account_number
        self.account_type = account_type
        self.account_status = account_status
        self.date_opened = date_opened
        self.balance = account_balance


    def details_of_account_owner(self):
        print("Name: ", self.owner_name)
        print("Account Number: ", self.account_number)
        print("Customer Type: ", self.account_type)
        print("Account Status: ", self.account_status)
        print("Date of opening: ", self.date_opened)
        print(f"Account Balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been successfully deposited into your account.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry, there is insufficient balance in your account.")
        else:
            self.balance -= amount
            print(f"${amount} has been successfully withdrawn from your account.")

    def display_balance(self):
        print(f"The current balance in your account is ${self.balance}.")

# Input account owner's details.
account_01 = BankAccount("James Smith", 123456, "Regular", "Active", "Jan 11 1999", 80000)
account_02 = BankAccount("Emily Johnson", 789012, "Regular", "Active", "Apr 10 2010", 1000)
account_03 = BankAccount("Benjamin William", 345678, "Premium", "Active", "Jan 12 1994", 3000000)
account_04 = BankAccount("Olivia Brown", 901234, "Regular", "Suspended", "Dec 20 2005", 1500)

print("Details of account owners:")
account_01.details_of_account_owner()
print("==================================")
account_02.details_of_account_owner()
print("==================================")
account_03.details_of_account_owner()
print("==================================")
account_04.details_of_account_owner()
print("==================================")

# Example of money deposit and withdraw process.
account_02.details_of_account_owner()
# Current balance is $1000.
# Deposit $2000 into Emily's account.

print( )
account_02.deposit(2000)
account_02.display_balance()
# Emily's current balance is $3000.
# Emily wants to withdraw $5000.
print()
account_02.withdraw(5000)
# There is not enough money in Emily's account balance.
# Then, Emily withdraw $2500 from her account.
account_02.withdraw(2500)
account_02.display_balance()
```
**Output**
```
Details of account owners:
Name:  James Smith
Account Number:  123456
Customer Type:  Regular
Account Status:  Active
Date of opening:  Jan 11 1999
Account Balance: $80000
==================================
Name:  Emily Johnson
Account Number:  789012
Customer Type:  Regular
Account Status:  Active
Date of opening:  Apr 10 2010
Account Balance: $1000
==================================
Name:  Benjamin William
Account Number:  345678
Customer Type:  Premium
Account Status:  Active
Date of opening:  Jan 12 1994
Account Balance: $3000000
==================================
Name:  Olivia Brown
Account Number:  901234
Customer Type:  Regular
Account Status:  Suspended
Date of opening:  Dec 20 2005
Account Balance: $1500
==================================
Name:  Emily Johnson
Account Number:  789012
Customer Type:  Regular
Account Status:  Active
Date of opening:  Apr 10 2010
Account Balance: $1000

$2000 has been successfully deposited into your account.
The current balance in your account is $3000.

Sorry, there is insufficient balance in your account.
$2500 has been successfully withdrawn from your account.
The current balance in your account is $500.

Process finished with exit code 0
```

