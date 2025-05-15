###CONJUNTOS

'''
Conjuntos, chamados em inglês de set são um tipo de dados que permitem armazenar outros tipos imutáveis ​​de uma forma não ordenada. 
Um item só pode estar contido em um conjunto uma vez. Não há duplicatas permitidas. 
Os benefícios de um conjunto são: ser capaz de usar operações de conjunto poderoso,
como union, difference, e intersection.
'''

'''
criação:
- set() (cria lista vazia) (1,) 
- {} fazer um dict vazio 
- {1,2,3} para varios items

met. comuns:

- meu_set.add(item) adicionar item, 
- minha_tupla.discard(item) remove item se estiver presente sem retorno de erro,
- minha_tupla.remove(item) retorna erro se o item não existir 
- meu_set.update(outro_set)
'''

'''
Ação	Método
Remove o elemento especificado e retorna None; se o elemento não existir, é gerado um KeyError	                            conjunto.remove(elemento)
Remove o elemento especificado e retorna None; se o elemento não existe, não gera um KeyError	                            conjunto.discard('elemento')
Remove um elemento arbitrário e retorna o elemento removido; se não houver o elemento, gera um KeyError	                    conjunto.pop()
Adiciona um determinado elemento ao conjunto; se o elemento estiver presente, não adiciona nenhum elemento	                conjunto.add(elemento)
Retorna uma cópia autônoma do conjunto	                                                                                    conjunto.copy()
Remove todos os elementos de um conjunto	                                                                                conjunto.clear()
Retorna os elementos diferentes da comparação de dois conjuntos; Não modifica os conjuntos originais	                    conjunto_01.difference(conjunto_02)
Atualiza o conjunto a partir das diferenças entre eles	                                                                    conjunto_01.difference_update(conjunto_02)
Retorna um novo conjunto com os elementos comuns aos conjuntos envolvidos na intersecção	                                conjunto_01.intersection(conjunto_02)
Atualiza o conjunto que chama o método com a intersecção dos conjuntos indicados; retorna um None	                        conjunto_01.intersection_update(conjunto_02)
Retorna True se dois conjuntos não apresentam elementos comuns; retorna False 
se os dois conjuntos apresentam elementos comuns; 
este método leva um único argumento e pode receber um iterável (lista, tupla, dicionário, string). 
Este método irá converter o iterável em um conjunto e verificará se os conjuntos são separados ou não	                    conjunto_01.isdisjoint(conjunto_02)
Retorna True se o subconjunto está dentro do conjunto. Caso contrário, retorna False.	                                    conjunto_01.issubset(conjunto_02)
Retorna True se set_a é um super conjunto do set_b. Caso contrário, retorna False	                                        conjunto_01.issuperset(conjunto_02)
Retorna os elementos que não estão na intersecção dos conjuntos	                                                            conjunto_01.symmetric_difference(conjunto_02)
Encontra os elementos que não fazem parte da intersecção e atualiza o conjunto pelo método	                                conjunto_01.symmetric_difference_update(conjunto_02)
retorna um novo conjunto com elementos únicos de todos os conjuntos relacionados na união	                                conjunto_01.union(conjunto_02)
Atualiza o conjunto que chama o método, adicionando elementos iteráveis; retorna None	                                    conjunto.update(elementos)

'''

###OPERAÇÕES DE CONJUNTOS
'''
Metodo	                                simbolo	                                resultado
s.union(t)	                           `s	                                    t`
s.intersection(t)	                    s & t	                                cria um novo conjunto contendo apenas itens que estão dentro s e dentro t
s.difference(t)	                        s ^ t	                                cria um novo conjunto contendo itens que não estão em ambos


'''