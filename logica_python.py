# criando variaveis
nome = "frazao"
sobrenome = "frazaozao"
idade = 167
altura = 2.67
adulto = False

# escrevendo no console 
print(nome)
print(sobrenome)
print(idade)
print(altura)
print(adulto)

# concatenando informações 
print('meu nome é', nome)
print('meu sobrenome é', sobrenome)
print('minha idade é', idade)
print('minha altura é', altura)
print('eu sou adulto?', adulto)

# maneira moderna (baianor) de concatenar informações
print(f'meu nome é {nome}')
print(f'meu sobrenome é {sobrenome}')
print(f'minha idade é {idade}')
print(f'minha altura é {altura}')
print(f'eu sou adulto? {adulto}')

# verificando o tipo da variavel
print(type(nome))
print(type(sobrenome))
print(type(idade))
print(type(altura))
print(type(adulto))

# expressões aritméticas
soma = idade + altura
subtracao = idade - altura
multiplicacao = idade * altura
divisao = idade / altura
print('soma:', soma)
print('subtração:', subtracao)
print('multiplicação:', multiplicacao)
print('divisão:', divisao)

# outras operações 
potencia = idade ** 2
div_exata = idade // altura
print('potência:', potencia)
print('divisão exata:', div_exata)