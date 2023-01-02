#QUESTION 2
def reciprocal(num):
	reciprocal = 1/num
	return round(recreciprocal, 5)

num = int(input("Enter a number: "))

if (num == 0):
	print("Number cannot be 0")
	if num in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
		print("Enter a valid number")
	print(statement)
else:
	def reciprocal(num):
		reciprocal = 1/num
		return round(reciprocal, 5)

print("the reciprocal of " + str(num) + " is " + str(reciprocal(num))


#QUESTION 3
name = input("enter your name: ")
invoice = str(input("enter invoice number: "))
payment = str(input("enter payment amount: ")) 

print invoice
invoice = ["15", '25', '66', '54', '69', '420', '87', '6', '85', '22', '36', '17', '14', '7', '5']

for i in (array_invoice) - 1:
	if invoice == array_invoice[i]:
		print(name + ", it is your lucky day, the amount to pay for invoice "
			+ str(invoice) + " is R" + str(payment) )
		if invoice != array_invoice[i]:
			print("Sorry, " + name + ", No luck today, the amount to pay for invoice "
		 + str(invoice) + " is R" + str(payment) )
#QUESTION 4
print("Miles to Kilometres speed converter appplication")

def speedconvert(speed):
kmh = speed * 1.609344
return kmh

def topspeed(speed1, speed2):
	if speed1 > speed2:
		top = speedconvert(speed1)
		print("The speed on the first day was the top speed")
		return top
		
	if speed2> speed1:
		top = speedconvert(speed2)
		print("The speed on the second day was the highest")
		return top

		if speed1 == speed2:
		top = speedconvert(speed1)
		print("The speed on both are the same")

while speedfdayone and speeddaytwo !=0:
	firstday = int(input("Enter first day speed in m/h: "))
	secondday = int(input("Enter second day speed in m/h: "))

	print("The speed for the first day in km/h is: " + speedconvert(firstday))
	print("The speed for the second day in km/h is: " + speedconvert(secondday))
	print("The top speed was: " + topspeed(firstday, secondday)



#QUESTION 5
name = input("enter your name: ")
age = int(input("enter your age: "))
avgscore = int(input("enter your average score in percentage %: "))
admission = True

if avgscore < 60:
admission = False
print("Unfortunately " + name + " you do not meet the requirements to be admitted to BscIT")

	if avgscore >= 60 and avgscore < 80 and age >= 30:
		print("Congratulations " + name + " you have been admitted for BscIT, you also qualify for a scholarship!")