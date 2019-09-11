import random


alpha_numeric = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%&*()_-+?|'

def gera_senha():
	length = random.randint(8, 15)
	i = 0
	pswd = ''

	while i<=length:
		pswd += random.choice(alpha_numeric)
		i+=1
	return pswd


if __name__ == '__main__':

	print(gera_senha())
