from aiohttp import web
from roman_marco import numero_para_romano
from validacpf_marco import Validator
from count_zero_marco import conta_zeros
from gera_senha_marco import gera_senha
from classificador_senhas_marco import classificar_senha
from hash_marco import hash_md5
import json


async def romano(request):
	num = request.match_info.get('numero', "Anonymous")
	num_roman = numero_para_romano(num)
	return web.Response(text=str(num_roman))


async def cpf(request):
	cpf = request.match_info.get('cpf', "Anonymous")
	val = Validator.valida_cpf(cpf)
	if val:
		return web.Response(text='Válido')
	else:
		return web.Response(text='Inválido')


async def zero(request):
	sentence = request.match_info.get('string', "Anonymous")
	zeros = conta_zeros(sentence)
	return web.Response(text=str(zeros))


async def senha(request):
	pwd = gera_senha()
	classifier_num = classificar_senha(pwd)
	classifier = ''
	if classifier_num == 0:
		classifier = 'Weak'
	elif classifier == 1:
		classifier = 'Medium'
	else:
		classifier = 'Strong'
	md5 = hash_md5(pwd)
	all = json.dumps({"password": pwd, "strength": classifier, "hash": md5})

	return web.Response(text=str(all))


app = web.Application()
app.add_routes([web.get('/romano/{numero}', romano),
		web.get('/valida_cpf/{cpf}', cpf),
		web.get('/dist_zeros/{string}', zero),
		web.get('/gera_senha/', senha)])


if __name__ == '__main__':
    web.run_app(app)
