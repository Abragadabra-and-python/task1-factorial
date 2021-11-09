# This function calculates the factorial
def factorial(iter):
	if iter == 0:
		return 1
	elif iter < 0:
		return 'Error! The number must be non-negative!'
	else:
		return iter * factorial(iter - 1)


print(factorial(5))