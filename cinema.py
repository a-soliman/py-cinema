films = {
	"Finding Dory": {
		"age": 3,
		"avilable_seats": 5
	},
	"Bourne": {
		"age": 18,
		"avilable_seats": 5
	},
	"Tarazan": {
		"age": 15,
		"avilable_seats": 5
	},
	"Ghost Busters": {
		"age": 12,
		"avilable_seats": 5
	}
}

while True:
	# Get the user's choice of film
	choice = input('Which movie would you like to watch?: ').strip().title()

	# check if the moview is avialable in the dict.
	if choice in films:
		age = int(input('How old are you?: ').strip())

		if age >= films[choice]["age"]:
			
			#check enough seats
			if films[choice]["avilable_seats"] > 0:
				print('Enjoy watching {}.'.format(choice))
				films[choice]["avilable_seats"] = films[choice]["avilable_seats"] -1
			
			else:
				print('No seats avialable...')

		else:
			print("You are too young for watching {}!".format(choice))		
	else:
		print("We don't have that film.")
