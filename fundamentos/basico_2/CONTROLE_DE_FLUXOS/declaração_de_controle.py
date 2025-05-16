###DECLARAÇÕES DE CONTROLE
    ##ALGORTIMO 
##CONDICIONAIS:
##IF;ELIF;ELSE

#EXEMPLO:

humor = "ótimo"

if humor == "ótimo":
    print("Solta o single e vai pro Coachella!")
elif humor == "mais ou menos":
    print("Posta uma foto misteriosa no Insta.")
else:
    print("Desaparece por um tempo, estilo Rihanna.")

'''
Comando for
range(),zip(), enumerate(), os.walk(), exclusão de linha
for no dict metodos
https://youtu.be/OSGv2VnC0go e video do Hash
'''

###EXEMPLO:
'''
colors = ["Red", "Green", "Blue", "Orange"]
for color in colors:
    print(f"The color is: {color}")
    
The color is: Red
The color is: Green
The color is: Blue
The color is: Orange
'''
###RANGE

##range(start, stop, step) e help(range)
'''
for num in range(5):
    print(f"The number is: {num}")
'''
##ENUMERATE
#enumerate (iteravel, start=0)
'''
Como enumerate()retorna uma estrutura que se parece com uma lista 
de tuples por baixo do capô, podemos aproveitar a descompactação da tupla no forloop.

'''


cores = ['azul', 'amarelo', 'vermelho','preto', 'branco', 'verde']

for index, item in enumerate(cores, start=1):
  print(f'Item: {item} é o indice: {index}')

###LAÇOS EM DICIONÁRIOS

#EXEMPLO
lusofonia = {"AmÃ©rica do Sul": "Brasil", "Europa": "Portugual", "Ãfrica":"Angola", "Ãsia":"Macau" }

for regiao in lusofonia:
    print(f"A região pe: {regiao}")
    
for luso, pais in lusofonia.items():
    print(f"A região é: {regiao} e o pais é: {pais}")
    
for  pais in lusofonia.values():
    print(f"O pais é: {pais}")


###Comandos if, elif, else

#EXEMPLO

# NÃO FAÇA ISSO
if (3 < 5) == True:
    print("Olá")

# NÃO FAÇA ISSO
if (3 < 5 ) is True:
    print("Olá")

# FAÇA ISSO
if 3 < 5:
    print("Olá")

# FAÇA ISSO

a = True
b = [1,2,3]

if a and b:
    print("Olá")

if a is True:
    print("Olá")

###Comando while

### BREAK, CONTINUE E RETURN
'''
Instrução	                        Detalhamento
return	                            A instrução return é usada para encerrar a execuçao de uma função e retornar o resultado para o chamador;
                                    as instruções indicadas abaixo a palavra-chave return não serão executadas;
                                    se a instrução return não tiver nenhuma expressão, None será retornado
break	                            A instrução break sairá completamente do loop atual, o que significa que não executará mais nenhuma das instruções contidas dentro deste loop
continue	                        A instrução continue volta para o início do loop atual
yield	                            A instrução yield retorna um resultado intermediário para o chamador, mas mantém o estado local da função, para que ela possa ser retomada exatamente de onde parou

'''

###Tratamento de exceções e tracebacks
##o basico de try e except

