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




name = ['jason', 'john', 'jack']

def greet():
    print('Hi there! ')
    print('How are you?')


greet()





def greet(name):
    return f"Hello {name}!"

message = greet('John')
print(message)


def hi(name):
    print(f"Hello {name}")

def greeting(name):
    return f"Hello {name}"

hi('Jason')
print(greeting('John'))



names = ['Jason', 'John', 'Michael', 'Rachel', 'Admin']
n = len(names)

for i in range(1,n):
    hi(names[i])




def hiAlvis():
    print('hi')

hiAlvis()

def say(something):
    print(something)

say('Hi alvis')
say('Hi Python')

def add(n1, n2):
    result = n1 + n2
    print(result)

add(1, 8)
add(8, 15)


def multiply(n1, n2):
    return n1*n2
value = multiply(1, 8) + multiply(8, 15)
print(value)



def numbers(max):
    sum = 0
    for n in range(1, max+1):
        sum+=n
    return sum
value = numbers(int(input('insert the number you want to add starting from 1')))
print(value)