##DEFINIÇÃO 
palavra = 'pneumoultramicroscopicossilicovulcanoconiótico'
print(palavra, type(palavra))

frase = 'O homem é o lobo do homem' 
print(frase, type(frase))

simbolos = 'áàUÜ#@^><阿萨' 
print(simbolos, type(simbolos))

##ASPAS DENTRO DE ASPAS


frase = 'O homem é o "lobo" do homem' 
print(frase, type(frase))

##BUILT-IN - INPUT()

novo_membro = input('digite o seu nome: ')
print('olá, ' + novo_membro)


### FORMATAÇÃO DE STRING 

#  f-string

novo_membro = input('digite o seu nome: ')
print(f'olá, {novo_membro}')

#format()

continente = 'ásia'
pais = 'china'
print('O país {1} está localizado no continente {0}'.format(pais, continente))

numero = 99
print('{:5d}'.format(numero))
print('olá, ' + novo_membro + '. Tudo bem com você?') 
print('Rafael ' * 10)

##INDICES E CARACTERES


"""
`[início:fim:salto]`
"""
linguagem = 'Python Slice String'
#A função len() indica o tamanho do tipo de dado. No caso da string, ela indica a quantidade de caracteres
print(len(linguagem))
#O print abaixo já mostra o primeiro elemento do conjunto de caracteres
print(linguagem[0])
#O print abaixo irá mostrar o último elemento da string
print(linguagem[-1])
#O print abaixo irá mostrar o intervalo entre o segundo e o quarto elemento 
print(linguagem[2:4])
#O print abaixo irá mostrar do primeiro ao quarto elemento 
print(linguagem[:4])
#O print abaixo irá mostrar do quarto elemento até o último
print(linguagem[3:])
#O print abaixo irá inverter a string 
print(linguagem[::-1])
#O print abaixo segue essa estrutura: `[início:fim:salto]`, assim começará no índice 1 e terminará no índice 19, saltando de 2 em 2
print(linguagem[1:19:2])
string_de_numeros = '0123456'
#O print abaixo começa no elemento 1 e vai até o último elemento saltando de 2 em 2, passando por todos os índices ímpares
print(string_de_numeros[1::2])
#O print abaixo verifica todos os elementos, saltando de 2 em 2, passando por todos os índices pares
print(string_de_numeros[::2])


'''
TIPOS DE DADOS"str"
uso:usado para armazenar uma lista de caracteres
criação:caracteres colocados "entre aspas"
métodos de buscar:find('elemento')
ordem preservada?	sim. os itens podem ser acessados por índices
mutável?	não
ordenado?	sim

'''

###MÉTODOS DE STRING 

from keyword import iskeyword 
#método split

novo_membro = input('digite o seu nome: ')
print(f'olá, {novo_membro}'.split(' '))


#método join
europa = ['portugal', 'espanha', 'italia']
print(type(europa))
europa_2 = ', '.join(europa)
print(europa_2)
print(type(europa_2))

#método strip
frase = '     roubei uma goiaba       '
print(frase.strip())

#métodos swapcase, upper, lower e title
frase = "Zen do Python"
print(frase.swapcase(), frase.upper(), frase.title(), frase.lower())

#método replace
print(frase.replace('Zen', 'Bravo'))

#método count
print(frase.count('n'), type(frase.count('n')))

#métodos startswith, endswith, find, isalnum, isalpha, isidentifier, iskeyword, isprintable, isspace, islower e isupper
frase = "Zen do Python"
print(frase.startswith("Zen"))
print(frase.endswith("do"))
print(frase.find('en do Python'))
print(frase.isalnum())
print(frase.isalpha())
print(frase.isidentifier())
print(iskeyword('return'))
print('x\ny'.isprintable())
print(' '.isspace())
print(frase.islower())
print(frase.isupper())

#método zfill
p = 'palavra'
print(p.zfill(8))

#métodos index e find
print(p.index('pa'))
print(p.find('pa'))


#CARACTERES DE ESCAPE - EXEMPLO 

print('meu nome é \n Fábio')
print('meu nome é \s Fábio')
print('meu nome é \t Fábio')
print('meu nome é \v Fábio')
print('meu nome é \e Fábio')
print('meu nome é\b Fábio')

