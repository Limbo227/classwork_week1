#problem 2
a = 2**3
b = 3**2
if a < b:
	print(a,'larger')
else:
	print(b,'larger')
#problem 22
a = 2
b = 4
c = 6
if a > c and a > b:
	print(a,'max')
	if b > c:
		print(c,'min')
	else:
		print(b,'min')
elif b > a and b > c:
	print(b,'max')
	if a > c:
		print(c,'min')
	else:
		print(a,'min')
else:
	print(c,'max')
	if a > b:
		print(b,'min')
	else:
		print(a,'min')
#problem 15
a = 17391 % 17
b = 546 % 17
c = 934 % 17
if a < b and a < c:
	print(a,'min%')
elif b < a and b < c:
	print(c,'min%')
else:
	print(c,'min%')
#problem 39
x = 13
if (x**2) < 179:
	x = x**2
#problem 5 
a = 30
if a % 2 == 0:
	print('четное число')
else:
	print('nechetnoe chislo')
if a % 3 == 0:
	print('chislo % 3 = 0')
else: 
	print('chislo % 3 = >0')
if (a**2) > 1000:
	print('chislo**2 > 1000')
else:
	print('chislo**2 < 1000')
#problem 3
chislo = 43
if (chislo > 20 and chislo < 57):
	print('chislo ne v diapozone')
#problem 7
a = 4
b = 4
if (a * 1) > (b*-1):
	print('srabotaet v lubom sluchae')
#problem 9
a = 5
if a == 5:
	if a % 5 == 0:
		if a*2==10:
			print('vse tri uslovia rabotaet')
#problem 45
a = 10//5
b = 10/5
if a == b:
	print(a+b)
else:
	print('chisla ne rovny')
#problem 33
if 100%2==0:
	print(-1,-2,-3)
#problem 11
a = 10
b = 5
if a > 0 and b > 0:
	print('polozhitelnye chisla')
#problem 0
a = 10
b = 5
if a > b:
	print(a+2)
else:
	print(b+2)

