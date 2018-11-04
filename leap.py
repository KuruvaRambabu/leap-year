a=2000
if (a%4)==0:
	if (a%100)==0:
		if (a%400)==0:
			print("a is the leap year",a)
		else:
			print ("a is not leap year",a)	
	else:
		print("a is leap year",a)
else:
	print("a is not not a leap year,a")		