# This function calculates the factorial
def factorial(iter):
	if iter == 0:
		return 1
	elif iter < 0:
		#Вместо возврата строки лучше вызвать ValueError
		#Так не рекомендую делать - return 'Error! The number must be non-negative!'
		#Лучше делать так:
		raise ValueError('The number must be non-negative!')
	else:
		return iter * factorial(iter - 1)

#В остальном всё ок
print(factorial(int(input('>>'))))
