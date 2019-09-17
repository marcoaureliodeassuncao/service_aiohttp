from aiohttp import web
from gera_senha_marco import gera_senha
from classificador_senhas_marco import classificar_senha
from hash_marco import hash_md5
from html_response import html_responser
import json


async def romano(request):
	num = request.match_info.get('numero', "Anonymous")
	num_roman = html_responser.romano(num)
	return web.Response(text=str(num_roman), content_type='html')


async def cpf(request):
	cpf = request.match_info.get('cpf', "Anonymous")
	val = html_responser.cpf(cpf)
	return web.Response(text=val, content_type='html')


async def zero(request):
	sentence = request.match_info.get('string', "Anonymous")
	zeros = html_responser.zero(sentence)
	return web.Response(text=str(zeros), content_type='html')


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
	all = html_responser.senha(pwd, classifier, md5)
	return web.Response(text=str(all), content_type='html')


app = web.Application()
app.add_routes([web.get('/romano/{numero}', romano),
		web.get('/valida_cpf/{cpf}', cpf),
		web.get('/dist_zeros/{string}', zero),
		web.get('/gera_senha/', senha)])


if __name__ == '__main__':
    web.run_app(app)
