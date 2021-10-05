person1 = {'name':'john','surname':'wick', 'age':36, }

#print(f"Name: {person1['name'].title()}, Surname: {person1['surname'].title()}, Age: {person1['age']}")

#print(f"Name: {person1['name'].title()}")
#print(f"Surname: {person1['surname'].title()}")
#print(f"Age: {person1['age']}")

person1['email'] = 'jwick@yahoo.com'
person1['male'] = True


#print(f"Email: {person1['email']}")
#print(f"Male: {person1['male']}")

person1['age'] = 30
del person1['male']

#print(person1)

info1 = person1['age']
#print(f"John's age is {info1}")

info2 = person1.get('eyecolor', 'No eyecolor assigned' )
#print(info2)

print('\nKey-Value Pairs:')
for k, v in person1.items():
	print(f"\t{k}: {v}")


print('\nKeys')
for k in person1.keys():
	print(f"\tKey: {k.title()}")

print('\nValues')
for v in person1.values():
	print(f"\tKey: {v}")
