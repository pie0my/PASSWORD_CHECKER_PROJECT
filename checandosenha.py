import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'error fetching: {res.status_code}, confira o API e tente denovo ')
    return res
# aqui sabemos que o res precisa ser 200, caso esteja em 400 não estaria dando certo, por isso damos o raise
# fazer um print e verificar caso necessário


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        print(h, count)


def pwned_api_checker(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # precisamos apenas dos 5 primeiros números quando queremos uma verificação de senha
    primeiros_5, resto = sha1password[:5], sha1password[5:]
    response = request_api_data(primeiros_5)
    print(response)
    return get_password_leaks_count(response, resto)

# lembrar de improtar o hashlib, caso duvida ler documentação
# checando a senha se ela existir na resposta do API
# em caso de duvida, ler sobre HASH


pwned_api_checker('123')
