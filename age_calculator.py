from datetime import datetime

def check_birthdate(year, month, day):
	# write code here
	birthdate = datetime(year, month, day)
	today = datetime.now()
	if birthdate > today:
		return False
	else:
		return True

def calculate_age(year, month, day):
    # write code here
	birthdate = datetime(year, month, day)
	today = datetime.now()
	difference = today - birthdate
	age_in_days = difference.days
	age = age_in_days // 365
	print("You are {} years old ".format(age))

def main():
	# write main code here
	year = int(input("Enter year of birth: "))
	month = int(input("Enter month of birth: "))
	day = int(input("Enter day of birth: "))

	if check_birthdate(year, month, day):
		calculate_age(year, month, day)
	else:
		print("birthdate is invalid")




if __name__ == '__main__':
	main()
