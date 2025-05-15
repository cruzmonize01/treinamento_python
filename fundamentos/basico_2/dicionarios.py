###DICIONARIOS
'''
Os dicionários são um tipo útil que nos permite armazenar nossos dados em pares de chave e valor. 
Os próprios dicionários são mutáveis , mas as chaves de dicionário só podem ser tipos imutáveis

'''
###DICT  (dicionário)

'''
Estrutura de dados dict	            
uso	                                Use para armazenar dados em pares de chave e valor. As chaves usadas devem ser tipos de dados imutáveis
criação	                            dict() ou {} (cria lista vazia) {key01: valor01, key02: valor02 } para varios items
métodos de buscar	                key in meu_dicionario
métodos comuns	                    meu_dicionario[key] para obter o valor da key e lançar um KeyError se a key não estiver no dicionário. Use meu_dicionario.get(key) para falhar silenciosamente se a key não estiver dentro meu_dicionario. meu_dicionario.items()para todas as chaves, pares de valores, meu_dicionario.keys() para todas as chaves e meu_dicionario.values() para todos os valores.
ordem preservada?	                Não, items não podem ser acessados por indice, apenas por chave
mutável?	                        Sim, é possivel adicionar ou remover items
pode ser reordenado?	            Não, por que dict não tem indices, apenas chaves
'''

'''
Ação	                                                                                                                            Método	                                                                retorno	                                possivel erro
remove todos os itens de um dicionário	                                                                                            meu_dicionario.clear()		
copia o dicionário original e os novos elementos colocados no novo dicionário não são acrescidos no original	                    meu_dicionario.copy()		
cria um novo dicionário a partir da sequência de elementos fornecidos	                                                            meu_dicionario.fromkeys(sequencia[, valor])		
retorna o valor da chave especificada	                                                                                            meu_dicionario.get('key')		
exibe os itens de um dicionário, sendo que eles são exibidos em uma lista e cada par chave-valor são elementos de uma tupla	        meu_dicionario.items()		
exibe uma lista de todas as chaves do dicionário	                                                                                meu_dicionario.keys()		
remove e retorna o último par de elementos inserido no dicionário	                                                                meu_dicionario.popitem()		
retorna o valor de uma chave ou insere a chave com o valor no dicionário	                                                        meu_dicionario.setdefault('key')		
remove e retorna um elemento de um dicionário com a chave fornecida	                                                                meu_dicionario.pop('key')		
retorna todos os "values" do dicionário	                                                                                            meu_dicionario.values()		
adiciona o elemento (chave-valor) se a chave não estiver no dicionário. Se achar, atualiza o dicionário	                            meu_dicionario.update()	
'''
#EXEMPLO:
turne = [
    {"cidade": "São Paulo", "look": "Onça com pedraria"},
    {"cidade": "Rio", "look": "Brilho holográfico"}
]

print(turne)
