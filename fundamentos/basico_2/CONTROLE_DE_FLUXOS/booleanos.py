###BOOLEANOS

#Avaliar se uma expressão é True ou False pode ajudar no controle de fluxo

###EXEMPLO

bool(0)      # False
bool(10)     # True
bool([])     # False
bool([1, 2]) # True
bool(None)   # False


###COMPARAÇÕES
'''
Operador	Significado
<	        Menor que
<=	        Menor ou igual que
>	        Maior que
>=	        Maior ou igual que
==	        Igual a
!=	        Diferente de
is	        identidade do objeto
is not	    identidade do objeto
'''

###OPERADORES BOOLEANOS

#OR;AND;NOT

#EXEMPLO:

com_saude = True
ensaio_vocal = True
envolvida_em_polemica = False

# A diva só sobe no palco se estiver saudável, tiver ensaiado E não estiver em polêmica
pode_subir_no_palco = com_saude and ensaio_vocal and not envolvida_em_polemica

print("A diva pode subir no palco?", pode_subir_no_palco)
if pode_subir_no_palco:
    print("🚨 PREPAREM OS HOLOFOTES: A DIVA VEM AÍ!")
else:
    print("😢 Infelizmente, a diva foi barrada. Quem sabe na próxima turnê...")
