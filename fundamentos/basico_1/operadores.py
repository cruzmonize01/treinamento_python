##OPERADORES EM STRING
'''
Operador	Descrição
+	        Concatenação de string
*	        Repetição de string
in	        Verifica se determinado caractere existe na string
not in	    Verifica se determinado caractere não existe na string
'''
continente = 'europa_'
pais = 'frança'
print(continente + ' ' + pais)
print(continente * 10)
print('f'in pais)
print('b'in pais)
print('b'not in pais)

###OPERADORES ARITMÉTICOS

'''

Operador	Descrição	                        Exemplo
+	Realiza a operação de adição	            5+5
-	Realiza a operação de subtração	            5-5
*	Realiza a operação de multiplicação	        5*5
/	Realiza a operação de divisão	            5/5
%	Resto da divisão	                        10%5
//	Divisão arredondada	                        22//5
**	Potenciação	                                5**2

'''

'''
Operadores Aritméticos
'''
print(5+5)
print(5-5)
print(5*5)
print(5/5)
print(10%5)
print(22//5)
print(5**2)

### OPERADORES DE ATRIBUIÇÃO

'''
Operadores de atribuição
'''
soma = 1
soma += 3 #Equivalente a `soma = soma + 3`
print(soma)
soma -= 2
print(soma)
soma *= 2
print(soma)
soma /= 2 #Lembre-se que toda divisão gera um tipo de dado `float`
print(soma)
soma = 1
soma ^= 3
print(soma)
soma >>= 3
print(soma)


###OPERADORES DE COMPARAÇÃO

'''
Operadores de Comparação
'''
x = 10
y = 20
print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)


###OPERADORES LÓGICOS OU BOLEANOS


##And;Or;NOt 

'''
Operadores lógicos ou booleanos
'''
a, b, c = 10, 15, 20
d = 10
print(a, b, c)
print(a > b and a > c)
print(a < b and a < c)
print(a == b or a == c)
print(a == b or a == c or a == d)
print(not a > b)

###OPERADORES  DE IDENTIDADE 

##Is; Is not

'''
Operadores de Identidade
Diferenciar operadores de identidade de operadores de comparação
'''
a = [5]
b = [5]
print(a is b)
print(a is not b)
print(a == b)


###OPERADORES DE MEMBROS OU DE ASSOCIAÇÃO

##In; not in;

'''
Operadores de membros ou de associação
'''
a = [5, 10, 15]
b = 'Brasil'
print(5 in a)
print('Brasil' not in a)
print('sil' in b)
print('Brasiu' in b)


###PRECEDENCIA DE OPERADORES

'''

Operador	                Descrição
or	                        Booleano or
and	                        Booleano and
not	                        Booleano not
==, !=, >=, <=, is, is not	Comparações e Identidades
+, -	A                   dição e Subtração
*, /, //, %	                Multiplicação, divisão, divisão arrendondada e resto da divisão
**	                        Exponenciação

'''
'''
Precedência
'''
a = 5
b = 10
c = 15
print(5 + 10**2)
print((5 + 10)**2)
print(a + b - c*a/b)
print(a + (b - c)*a/b)


###CONVERSÃO DE TIPOS

'''
Conversão de tipos de dados simples
'''
a = 'Brasil'
b = 10
c = 15.5
print(type(a))
print(type(b))
print(type(c))
print(int(c))

b = str(b)
print(type(b))

