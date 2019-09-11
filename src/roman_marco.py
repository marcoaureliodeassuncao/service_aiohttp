import sys


num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
	   (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'),
	   (4, 'IV'), (1, 'I')]


def valida_numero(num):

	if num.isalpha():
		return False
	num = float(num)
	if int(num) <= 0 or int(num) >= 4000:
		return False
	return True


def numero_para_romano(num):

	roman_num = ''

	if valida_numero(num):
		num = float(num)
		num = int(num)
		for i, r in num_map:
			while int(num) >= i:
				roman_num += r
				num -= i
		return roman_num
	else:
		return False


if __name__ == '__main__':
	print(valida_numero(sys.argv[1]))
	print(numero_para_romano(sys.argv[1]))
