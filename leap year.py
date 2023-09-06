def  isLeapYear(year):
	if(year%4==0 and year%100!=0)or year%400==0:
		return True
	else:
		return False
year=int(input("enter a year:"))
if isLeapYear(year):
	print('{} is a leapy(ear:'.format(year))
else:
	print('{} is a not a leapyear:'.format(year))