import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + '51BAE'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'error fetching: {res.status_code}, confira o API e tente denovo ')
# aqui sabemos que o res precisa ser 200, caso esteja em 400 não estaria dando certo, por isso damos o raise
# fazer um print e verificar caso necessário


def pwned_api_checker(password):
    sha1password = hashlib.sha1(password.encode('utf-8'))

# lembrar de improtar o hashlib, caso duvida ler documentação
# checando a senha se ela existir na resposta do API
# em caso de duvida, ler sobre HASH


pwned_api_checker('123')
