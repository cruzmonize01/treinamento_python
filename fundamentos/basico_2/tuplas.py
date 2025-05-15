###TUPLAS
    ##Nas tuplas os dados permanecem inalterados


###Estrutura de dados tuple	
uso	
criação	                () ou tuple() (cria lista vazia) (1,) para um item ou (1,2,3) para varios items
métodos de buscar	    minha_tupla.index(item) or item in minha_tupla
métodos comuns	        Não é possivel adicionar or remover itens. Então apenas minha_tupla.count(item) contar itens da tupla e minha_tupla.index(item) operam sobre tuplas
ordem preservada?	    sim. os itens podem ser acessados por índices
mutável?	            não
pode ser reordenado?	não




estudante = ("João", 21, "História das Relações Internacionais", 10.0)

nome, idade, disciplina, nota = estudante

def http_status_code():
...     return 200, "OK"
...
code, value = http_status_code()



