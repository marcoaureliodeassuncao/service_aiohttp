from roman_marco import numero_para_romano
from validacpf_marco import Validator
from count_zero_marco import conta_zeros
from gera_senha_marco import gera_senha
from classificador_senhas_marco import classificar_senha
from hash_marco import hash_md5


class html_responser:


	def home():
		content = '''<html>
    <head>
        <meta charset="UTF-8">
    </head>
	<body>
	    <h1>Home</h1>
	    <script type="text/javascript">
			function Romanizer(){
				var dec=document.getElementById("RomanForm").value;
				window.location = "http://localhost:8080/romano/" + dec;
				return false;
			}
		</script>
		<script>
			function ValidateCPF(){
				var cpf=document.getElementById("ValidatorForm").value;
				window.location = "http://localhost:8080/valida_cpf/" + cpf;
				return false;
			}
		</script>
		<script>
			function ZeroCounter(){
				var zero=document.getElementById("ZeroForm").value;
				window.location = "http://localhost:8080/dist_zeros/" + zero;
				return false;
			}
		</script>
		<script>
			function GeneratePassword(){
				window.location = "http://localhost:8080/gera_senha/";
				return false;
			}
		</script>
		<form method="POST" action="">
			<label>Input a number: </label>
			<input type="text" name="num_dec" id="RomanForm">
			<input type="button" value="Romanize" onclick="Romanizer()"/>
		</form>
		<form method="POST" action="">
			<label>Input your CPF: </label>
			<input type="text" name="cpf" id="ValidatorForm">
			<input type="button" value="Validate" onclick="ValidateCPF()"/>
		</form>
		<form method="POST" action="">
			<label>Input an sentence with zero's: </label>
			<input type="text" name="zero" id="ZeroForm">
			<input type="button" value="Counter" onclick="ZeroCounter()"/>
		</form>
		<form>
			<label>Generate a password</label>
			<input type="button" value="Generate" onclick="GeneratePassword()"/>
		</form>
	</body>
</html>
'''
		return content

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

