#Sortear numeros aletatorios e nao repetidos para aposta da mega da virada
from random import sample

# Calculo ddo valor total das apostas
valor_aposta = float(3.50)
print('R${:.2f}'.format(valor_aposta))

# Sugestoes de numeros para apostar
numero_de_apostas = int(input('Quantas apostas voce gostaria de fazer?'))

def sugestoes_de_numeros():
    i=0
    lista_de_numeros = sample(range(1,61),6)
    while i < numero_de_apostas:
        print(lista_de_numeros)
        lista_de_numeros = sample(range(1,61),6)
        i = i + 1

n = int(input('Gostaria que eu te sugerisse alguns numeros?\n(1)SIM (2)NÃO\n'))    

if (n == 1):
    sugestoes_de_numeros()
elif(n == 2):
    input('Boa sorte entao!')
else:
    input('Resporta incorreta!')    
