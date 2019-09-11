import sys


def conta_zeros(string_1):
	count = 0
	aux = 0
	string_1 = string_1.strip()
	for i, character in enumerate(string_1):
		if character == '0':
			count+=1
		if i == len(string_1)-1:
			if count >= aux:
				aux = count
		else:
			if character == '0' and string_1[i] != string_1[i+1]:
				if count > aux:
					aux = count
				count = 0

	return aux


if __name__ == '__main__':
	string_1 = str(sys.argv[1:])
	print(string_1)
	print(conta_zeros(string_1))


