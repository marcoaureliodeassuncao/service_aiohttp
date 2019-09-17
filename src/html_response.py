from roman_marco import numero_para_romano
from validacpf_marco import Validator
from count_zero_marco import conta_zeros
from gera_senha_marco import gera_senha
from classificador_senhas_marco import classificar_senha
from hash_marco import hash_md5


class html_responser:


	def romano(num):
		content = '''<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
	<h1 style = "font-family:georgia,garamond,serif;font-size:16px;font-style:italic;">Roman</h1>
	<p style = "font-family:georgia,garamond,serif;font-size:16px;font-style:italic;">Decimal: {}</p>
      <p style = "font-family:georgia,garamond,serif;font-size:16px;font-style:italic;">Romano: {}</p>
</body>
</html>
'''.format(num, numero_para_romano(num))
		return content

	def cpf(cpf):
		content = '''<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
	<h1 style = "font-family:verdana;font-size:20px;color:red;">CPF Validator</h1>
	    <p style = "font-family:verdana;;font-size:20px;color:red;">CPF: {}</p>
        <p style = "font-family:verdana;;font-size:20px;color:red;">Válido: {}</p>
</body>
</html>
'''.format(cpf, Validator.valida_cpf(cpf))
		return content

	def zero(sentence):
		content = '''<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
	<h1 style = "font-family:courier;font-size:36px;color:blue;">Zero Counter</h1>
	    <p style = "font-family:courier;font-size:36px;color:blue;">Sentença: {}</p>
        <p style = "font-family:courier;font-size:36px;color:blue;">Zeros: {}</p>
</body>
</html>
'''.format(sentence, conta_zeros(sentence))
		return content

	def senha(pwd, classifier, md5):
		content = '''<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
	<h1 style = "font-family:TimesNewRoman,serif;font-size:48px;color:green;">Password</h1>
	    <p style = "font-family:TimesNewRoman,serif;font-size:48px;color:green;">senha: {}</p>
	    <p style = "font-family:TimesNewRoman,serif;font-size:48px;color:green;">strength:{} </p>
        <p style = "font-family:TimesNewRoman,serif;font-size:48px;color:green;">hash: {}</p>
</body>
</html>
'''.format(pwd, classifier, md5)
		return content

