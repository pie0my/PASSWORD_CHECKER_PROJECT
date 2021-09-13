import requests
import hashlib
import sys


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
        if h == hash_to_check:
            return count
    return 0


def pwned_api_checker(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # precisamos apenas dos 5 primeiros números quando queremos uma verificação de senha
    primeiros_5, resto = sha1password[:5], sha1password[5:]
    response = request_api_data(primeiros_5)
    return get_password_leaks_count(response, resto)

# lembrar de improtar o hashlib, caso duvida ler documentação
# checando a senha se ela existir na resposta do API
# em caso de duvida, ler sobre HASH
# resto (tail em ingles) é a parte da senha que ninguém tem


def main(args):
    for password in args:
        count = pwned_api_checker(password)
        if count:
            print(
                f'{password} foi encontrado {count} vezes, você deveria trocar a senha')
        else:
            print(f'{password} não foi encontrado, boa senha')
    return 'feito'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
