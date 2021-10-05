motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#motorcycles[0] = 'ducati'
motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(1, 'bmw')
print(motorcycles)


#Deletes by index
del motorcycles[0]
print(motorcycles)

#deletes by value
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

#delete by value
#motorcycles.remove('ducati')
#print(motorcycles)


first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)