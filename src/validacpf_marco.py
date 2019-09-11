import sys


class Validator:

	@classmethod
	def retira_formatacao(self, num_cpf):
		for element in num_cpf:
			if not element.isdigit() and element not in ['.','-']:
				return False
		return num_cpf.replace(".","").replace('-','')

	@classmethod
	def valida_cpf(self, num_cpf):
		n = 10
		v = 0
		try:
			cpf_formatado = Validator().retira_formatacao(num_cpf)
		except TypeError:
			return False
		try:
			if len(set(list(cpf_formatado))) == 1:
				return False
			else:
				list_1 = list(cpf_formatado[:9])
				for number in list_1:
					v += int(number)*n
					n -=1
				if v*10%11 == int(cpf_formatado[-2]):
					n2 = 11
					v2 = 0
					list_2 = list(cpf_formatado[:-1])
					for number in list_2:
						v2+=int(number)*n2
						n2-=1
					if v2*10%11 == int(cpf_formatado[-1]):
						return True
					else:
						return False
				else:
					return False
		except (TypeError, IndexError) as error:
			return False


if __name__ == '__main__':

	print(Validator().retira_formatacao(sys.argv[1]))
	print(Validator().valida_cpf(sys.argv[1]))

