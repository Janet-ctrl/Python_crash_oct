#4.1 Make a for loop
pizzas = ['seafood', 'cheddament', 'chicken']

for pizza in pizzas:
	print(f'The {pizza.title()} pizza is amazing')

print(f'\nI really like pizza!')

#4.2 
pets = ['cat', 'dog', 'goldfish']

for pet in pets:
	print(f'A {pet} is an easy pet to manage.')

print(f'All these animals can be great pets.') 

#4.3 Count to 20 
numbers = list(range(1,21))
print(numbers)

#4.4 One million
'''numbers2 = list(range(1, 1_000_001))
print(numbers2)'''

#4.5 Summing a Million
numbers2 = list(range(1, 1_000_001))
print(min(numbers2))
print(max(numbers2))
print(sum(numbers2))

#4.6 Odd numbers
odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

#4.7 Threes
three_numbers = list(range(3, 31, 3))
print(three_numbers)

#4.8 Cubes -eish
cubes = []
for value in range(1,11):
	cube = value**3
	cubes.append(cube)
print(cubes)

#4.9 Cube comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)

#4.10 slice three items.
print(f'\n\n\n')
pizzas = ['seafood', 'cheddament', 'chicken', 'hawaian', 'three cheese', 'meaty']

#first 3
print(f'The first three items in the list are:{pizzas[0:3]}')
#middle 3
print(f'The middle three items in the list are:{pizzas[2:5]}')
#last 3
print(f'The last three items in the list are:{pizzas[3:7]}')

#4.11
friend_pizzas = ['seafood', 'cheddament', 'chicken', 'hawaian', 'three cheese', 'meaty']
