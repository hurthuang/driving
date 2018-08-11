country = input('請問您是哪個國家？')
age = input('請問您幾歲？')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你不能考駕照')
elif country == 'USA':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你不能考駕照')