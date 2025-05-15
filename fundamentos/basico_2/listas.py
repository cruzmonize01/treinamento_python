###LISTAS



##criação:[] ou list() (cria lista vazia) ou [1,2,3]
##met. comuns:len(minha_lista) quantidade de elementos
##ordem preservada? sim
##mutável?sim


Ação	                                                                                                        Método	                                                        retorno	                                            possivel erro
checar tamanho	                                                                                                len(minha_lista)	                                            int	
adicionar no final da lista	                                                                                    minha_lista.append(item)		
adicionar itens de outra lista	                                                                                minha_lista.extend(item)		
saber indice do item	                                                                                        minha_lista.index(item)		
inserir em posição determinada da lista	                                                                        minha_lista.insert(posição, item)		
remover item da lista	                                                                                        minha_lista.remove(item)		
remover o último item ou um item pelo indice	                                                                minha_lista.pop() ou minha_lista.pop(pos)		
exclui um elemento a partir de um determinado índice e remove fatias de uma lista	                            del minha_lista[n1:n2]		
remove todos os itens de uma lista	                                                                            minha_lista.clear()		
quantidades de vezes que determinado item aparece na lista	                                                    minha_lista.count(item)		
copia a lista original e os novos elementos colocados na nova lista não são acrescidos na lista original	    minha_lista.copy()		
classifica os elementos da lista em ordem crescente ou decrescente, muda a lista diretamente	                minha_lista.sort()		
não muda a lista, simplesmente ordena	                                                                        sorted(minha_lista)		
inverte os elementos da lista	                                                                                minha_lista.reverse()		
atualização na posição	                                                                                        minha_lista[posição] = item		
procurar item na lista	                                                                                        item in minha_lista		

