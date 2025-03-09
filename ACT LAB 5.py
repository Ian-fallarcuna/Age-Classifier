def classify_age(age):
	if age < 0:
		print("invalid age, it cannot be negative")
	elif age <= 12:
		print("You are only a child")
	elif age <= 19:
		print("You are a teenager")
	elif age <= 64:
		print("You are an adult")
	else:
		print("You are too old")
		
while True:
	age = int(input("Enter your age: "))
	classify_age(age)