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
			print('Agreed')
		else:
			print("You are too young for this movie")		
	else:
		print("We don't have that film.")
