###MUTABILIDADE

'''
O que chamamos aqui de tipos de dados avançados também é chamado na documentação oficial de built-in containers. 
Em geral, o termo built-in se refere a aspectos oferecidos nativamente pelo Python, ou seja, são aspectos que estão 
disponíveis por padrão na linguagem,não sendo necessário a utilização de bibliotecas de terceiros. 
Já o termo containers se refere a tipos de dados sequenciais, de conjuntos, de mapeamento.
 Deste modo, como veremos a seguir, tipos de dados como listas, tuplas, dicionários, conjuntos, são chamados de built-in containers
'''

#EXEMPLO:

# Lista: diva que adora mudar o look
look = ["batom vermelho", "cabelo cacheado"]
look.append("brinco brilhante")  # Tá trocando de look, adicionando brilho!
print(look)
# Output: ['batom vermelho', 'cabelo cacheado', 'brinco brilhante']

# Tupla: diva clássica, look fixo
look_tupla = ("batom vermelho", "cabelo cacheado")
# look_tupla.append("brinco")  # Isso aqui não rola, diva não muda o look!


###ORDEM
'''
Ordenado ≠ Não ordenado

'''

