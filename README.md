# PASSWORD_CHECKER_PROJECT
Construção de um password checker.


Projeto finalizado, mas pode ser adicionado uma checagem por meio de um bloco de notas no sys


MOMENTO 1:
1 -No primeiro momento foi baixado o requtests do PyPI, para podermos fazer um request e utilizar funcionalidades do https://haveibeenpwned.com/Passwords, para isso utilizamos como URL a API do site + a senha (query_char) que seria colocada no site. Assim ja podemos iniciar nossa função request_api_data(query_char).
2 - Para sabermos se esta funcionado utilizamos o request com o method get(url), com resposta desejada de 200.
3 - Existe um erro esperado, aqui usaremos o raise para caso esse erro ocorra e ja direcionarmos nossos esforços.

MOMENTO 2:
4 - Importamos o hashlib que é um modulo de construção para fazer nosso SHA1 hashing (caso necessário leia sobre o que é hash e passwords)
5 - Para possibilitar "HASHEAR" minha senha, definimos sha1password utilizando metodos do hashlib : hashlib.sha1(password.encode('utf-8')).hexdigest().upper(), aqui é aconselhado ler a documentação, mas em linhas gerais, temos criação algoritimos hexadecimais, letras maiusculas,e em geral transformação da senha para o formato que é utilizado na HASH.
6 - Precisamos apenas dos 5 primeiros caracteres quando queremos uma verificação de senha, normalmente é assim que temos checagem, entretanto para decifrar a senha completa, é necessário todo número HASH criado, por isso dividiermos em primeiros 5 caracteres e o resto
7 - Para checar se esta funcionando, criamos nosso response, utilizando a primeira função de request_api_data() e colocando como query_char nossos 5 primeiros números, que acaba sendo como o site funciona na checagem dos HASHs

MOMENTO 3:
8 - Para checar o que é feito quando estamos fazendo a checagem com o response, fizemos um print(response.text), que depois foi apagado, mas foi utilizado para entender como funciona a checagem de senhas. É possivel ver todas as senhas que o request_api_data testa e quantas vezes foi invadido, que coincidem com os primeiros 5 caracteres HASH que utilizamos.
9 - Para checar se especificamente a nossa senha foi hackeada é necessário então saber todo nosso codigo HASH, utilizando o "resto" para fazer essa testagem.
10 - Criamos o get_password_leaks_count(hashes, hash_to_check), que seão respectivamente, os hash codes e o resto.
11 - Criamos:
hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:

Aqui foi feita a divisão do hash e da contagem de vezes que as senhas foram invadidas, então o split inicial é apos os ":" e o text.splitlines() foi utilizado para o loop realizar a exposição das senhas de maneira linear (sem ter quebras de linhas em cada caracteres).
12 - o h == hash_to_check acontece porque o resto é uma parte da senha que ninguem possui, apenas nós mesmo, portanto se forem == saberemos se exatamente nossa senha foi hackeada.

MOMENTO 4:
13 - Uma ultima coisa deve ser feita, que é print de todos nossos calculos e possibilidades, e fizemos isso com o "main(args)", utilizando o modulo sys.
14 - Faremos um loop em cada password do nossos args e como o count esta dentro do password_leaks, podemos fazer count = count = pwned_api_checker(password).
15 - if count existir, faremos uma string falando que a senha é fraca, porque se o count existe ele foi hackeado
16 - else é o return 0 que significa sem nenhuma invasão.

MOMENTO 5:
17 - Finalizamos no caso de executar apenas se for o MAIN
