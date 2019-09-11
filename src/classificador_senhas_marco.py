import sys
import re


'''critérios para determinar a classificação das senhas:
	- A senha deve conter pelo menos um caractere lower case,
	um caractere upper case, um número, um caractere especial e ter pelo menos
	8 caracteres;

	- a senha que não obedecer a todos esse critérios será categorizada
	como low;

	- senhas que obedeceram esses critérios mas possuem tamanho entre
	8 a 12 caracteres são categoriazadas como medium;

	- senhas acima de 12 caracteres e que obedeçam os critérios serão
	categorizadas como strong
'''


def classificar_senha(senha):
	flag = 0
	reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
	pat = re.compile(reg)

	if ' ' in senha:
		return False

	if len(senha) < 8:
		return flag

	elif len(senha)>8 and len(senha)<=12:
		if re.search(pat, senha):
			flag+=1
		return flag

	elif len(senha)>12:
		flag+=1
		if re.search(pat, senha):
			flag+=1
		else:
			flag-=1
		return flag


if __name__ == '__main__':

	print(classificar_senha(sys.argv[1]))

