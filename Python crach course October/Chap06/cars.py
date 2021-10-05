cars = {
'Ford': {
			'make': 'Ranger',
			'model': 2017,
			'milage': 120_000,
			},
'Dodge':{
		'make':'Ram',
		'model': 2009,
		'milage': 89_000,
		},
}

for car, car_info in cars.items():
	print(f"\nCar: {car}")
	car_details = f"{car_info['make']} {car_info['model']}"
	milage = car_info['milage']
	print(f"Vehicle: {car_details.title()}")
	print(f"Milage: {milage}")







