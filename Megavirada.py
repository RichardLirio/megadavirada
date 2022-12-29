#Sortear numeros aletatorios e nao repetidos para aposta da mega da virada
from random import sample
premio_mega = float(500000000)
valor_aposta = float(3.50)
numero_de_pessoas = int(input('Quantas pessoas participarão do bolão?\n'))
valor_bolao = int(input('Qual o valor que cada participante irá pagar?\n'))
numero_de_apostas=int((valor_bolao*numero_de_pessoas)/valor_aposta)

# Calculo ddo valor total das apostas e premio
def valor_total_apostas():
    print('O bolão poderá realizar {} apostas'.format(numero_de_apostas))
    print('Caso voces sejam sorteados cada participante receberá R${:.2f}'.format(premio_mega/numero_de_pessoas))

# Sugestoes de numeros para apostar
def sugestoes_de_numeros():
    i=0
    lista_de_numeros = sample(range(1,61),6)
    while i < numero_de_apostas:
        print(lista_de_numeros)
        lista_de_numeros = sample(range(1,61),6)
        i = i + 1

n = int(input('Gostaria que eu te sugerisse alguns numeros para apostar?\n(1)SIM (2)NÃO\n'))    

if (n == 1):
    sugestoes_de_numeros()
    valor_total_apostas()
    input('Boa sorte!')
elif(n == 2):
    valor_total_apostas()
    input('Boa sorte entao!')
else:
    input('Resporta incorreta!')    
