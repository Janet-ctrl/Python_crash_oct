#requested_topping = 'mushrooms'

#if requested_topping != 'anchovies':
	#print("Hold the anchovies!")


requested_toppings = ['mushrooms', 'onions', 'pineapple']

#requested_topping = 'pepper'

#if requested_topping in requested_toppings:
#	print(f'The requested topping {requested_topping} is available.')
#else:
#	print(f'The requested topping {requested_topping} is NOT available.')


#multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']

#	print("Adding mushrooms.")
#if 'pepperoni' in requested_toppings:
#	print("Adding pepperoni.")
#if 'extra cheese' in requested_toppings:
#	print("Adding extra cheese.")
#	print("\nFinished making your pizza!")

#requested_toppings = ['mushrooms', 'extra cheese']
#if 'mushrooms' in requested_toppings:
#elif 'pepperoni' in requested_toppings:
#	print("Adding pepperoni.")
#elif 'extra cheese' in requested_toppings:
#	print("Adding extra cheese.")
#	print("\nFinished making your pizza!")


available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")
		print("\nFinished making your pizza!")