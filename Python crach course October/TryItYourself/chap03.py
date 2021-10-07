#3.1
names = ['Nicolene', 'Dolene', 'Maryka', 'Ruda', 'Ronel']
print(names[0])
print(names[-1])
print(names[1])
print(names[3])
print(names[2])



#3.2
names = ['Nicolene', 'Dolene', 'Maryka', 'Ruda', 'Ronel']
message = (f"Would you like to have some cake?")
print('\n\n')
print(f'{names[0]}, {message}')
print(f'{names[-2]}, {message}')
print(f'{names[1]}, {message}')
print(f'{names[4]}, {message}')
print(f'{names[-3]}, {message}')
print('\n\n\n')



#3.3
car = ['Ford Ranger', 'Dodge Ram', 'Toyota Hilux', 'Amarok']
statement1 = f"Red is a good color for a {car[1]}!"
statement2 = f"A {car[0]} is very feul effecient."
statement3 = f"{car[-2]} is not my favorite on the list..."
statement4 = f"The {car[-1]} looks like a bulky vehicle."

print(f'A list of big cars: {car}')
print('\n')
print(statement4)
print(statement3)
print(statement1)
print(statement2)


#3.4
guest = ['Elvis', 'Sannie', 'Tante Koba']
invite = f"Come Party!"

print('\n'f"Hello {guest[0]}, {invite}")
print('\n'f"Hello {guest[1]}, {invite}")
print('\n'f"Hello {guest[-1]}, {invite}")

#3.5
guest = ['Elvis', 'Pietie', 'Tante Koba']
invite = f'Come Party!'


print(f'\nHaloo {guest[2]}! {invite}')
print(f'\nHi!! {guest[0]}! {invite}')
print(f'\nHey {guest[1]}!! {invite}')

print(f'\nAwww, {guest[0]} can\'t make it.. Too bad.\n')

#guest list
print(f'This is out guest list {guest}\n')
#replacing guest
del guest[0]
guest.insert(0, 'Ouma Hettie')
print(f'And this is the updated list!! {guest}')
print(f'\nHi!! {guest[0]}! {invite}')
print(f'\nHi!! {guest[2]}! {invite}')
print(f'\nHey {guest[1]}!! {invite}')

#3.6
print(f'\n Hi guys! I found a bigger table! The more the marrier!')
guest.insert(0, 'Karel kat')
guest.insert(2, 'Liewe Heksie')
guest.append('Koning Rosedoring')
print(f'{guest}')

print(f'\nHi!! {guest[0]}! {invite}')
print(f'\nHi!! {guest[1]}! {invite}')
print(f'\nHey {guest[2]}!! {invite}')
print(f'\nHi!! {guest[3]}! {invite}')
print(f'\nHi!! {guest[-2]}! {invite}')
print(f'\nHey {guest[-1]}!! {invite}')

#3.7
print(f'\nHi guys! Bad news, covid restrictions upped. I can only invite two people. So sorry.')
guest.pop(0)
guest.pop(0)
guest.pop(0)
guest.pop(0)
print(f'\nAmended guest list:{guest}')
print(f'\nHi!! {guest[0]}! You are still invited. {invite}')
print(f'\nHi!! {guest[1]}! You are still invited. {invite}')
print(f'\nHi guys! Bad news, covid restrictions upped. The event is cancelled.')
del guest[:]
print(f'{guest}\n')

#3.8
"""Places I want to see"""
places = ['Nuuk, greenland','Fussen, Germany', 'Rocky Mountains, Canada','Maui, Hawaii', 'Rome, Itally', ] 
#list in original order
print(f'{places}')
#List temporarily sorted
sorted(places)
#original list
print(f'{places}')
#sorted alphabetically and reversed ***
print(f'{sorted(places, reverse = True)}')
#original list
print(f'{places}')
#reverse list permanently
places.reverse()
print(f'{places}')
#change list again
places.reverse()
print(f'{places}')
#alphabetical order
places.sort()
print(f'{places}')
#reverse alphabetical
places.reverse()
print(f'{places}')


#3.9
guest = ['Elvis', 'Pietie', 'Tante Koba']

print(f'{len(guest)}')


#3.10
print(f'\n\n')
#List of sporting hobbies
hobbies = ['Water ski', 'Jet Ski', 'Game hunting', 'Competition Shooting', 'Quadbike Riding']
print(hobbies)

#sort hobbies alphabetically permenantly
print(f'\n')
hobbies.sort()
print(hobbies)

#reverse sort
print(f'\n')
hobbies.reverse()
print(hobbies)

#temporary sort
print(f'\n')
print(sorted(hobbies))

#remove and reassign quadbikung to offroad hobby
print(f'\n')
offroad_hobby = hobbies.pop(-1)
print(f'\n{offroad_hobby} can be enjoyed by all ages.\n')

#insert a hobby at the front
print(f'\n')
hobbies.insert(0, 'Mountain biking')
print(hobbies)

#add hobby at the end of the list
print(f'\n')
hobbies.append('bi-athalon')
print(hobbies)

#delete bi-athalon
print(f'\n')
del hobbies[-1]
print(hobbies)

#reverse alphabetize the list
print(f'\n')
hobbies.sort()
hobbies.sort(reverse=True)
print(hobbies)

#count the lenth of the list
print(f'\n')
total = len(hobbies)
print(f'I have a total of {len(hobbies)} hobbies.')

#check the index number of 'Jet Ski'
print(f'\n')
print(hobbies.index('Jet Ski'))

#make a copy of the list
print(f'\n')
print(hobbies.copy())

#remove the element with the index value of 3
print(f'\n')
print(f'This is all the hobbies: {hobbies}.')
hobbies.remove('Jet Ski')
print(hobbies)

#cleat the list out
print(f'\n')
hobbies.clear()
print(f'Time for a new adventure, my current hobby list is: {hobbies} lets start fresh.')


#3.11
fruits = ['bananna', 'strawberry', 'orange', 'kiwi']
#print(fruits[4]) - index error

#correct index search
print(fruits[-1])

print(fruits[3])
