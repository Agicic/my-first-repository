valtozo="valtozo"
for szam in range(100):
	szam=szam+1
	if szam%3!=0:
		if szam%5!=0:
			print (szam)
		else:
			valtozo="Buzz"
			print(valtozo)
	else:
		if szam%5==0:
			valtozo="Fizzbuzz"
		else:
			valtozo="Fizz"
		print(valtozo)
