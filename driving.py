country = input('Your Nationality: ')
age = int(input('Your age: '))
if country == 'Taiwan':
	if age >= 18:
		print('You are allowed to go for a driving test.')
	else :
		print('You are NOT allowed to go for a driving test.')
elif country == 'USA':
	if age >= 16:
		print('You are allowed to go for a driving test.')
	else :
		print('You are NOT allowed to go for a driving test.')
else :
	print('Only Taiwan and USA are allowed for this so far.')