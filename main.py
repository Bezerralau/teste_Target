# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def verifica_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
print(verifica_fibonacci(numero))

import json



# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# O menor valor de faturamento ocorrido em um dia do mês;
# O maior valor de faturamento ocorrido em um dia do mês;
# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
import json

with open('faturamento_mensal.json', 'r') as file:
    faturamento_diario = json.load(file)


faturamento_diario = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]


menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)
media_mensal = sum(faturamento_diario) / len(faturamento_diario)
dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias com faturamento acima da média mensal:", dias_acima_media)



#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
#Outros – R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_mensal = sum(faturamento_por_estado.values())
percentuais_por_estado = {estado: (faturamento / total_mensal) * 100 for estado, faturamento in faturamento_por_estado.items()}




# 5) Escreva um programa que inverta os caracteres de um string.
def inverter_string(s):
    inverted = ''  
    for i in range(len(s) - 1, -1, -1):  
        inverted += s[i]  
    return inverted

string = input("Informe uma string: ")  
print("String invertida:", inverter_string(string))  

