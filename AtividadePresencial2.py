import random
somatorio = 0
multiplicacao = 1
lista_randomica=[]

n = int(input(f"Digite de repetiçoes: "))
for i in range(n):
    numero = random.randint(0,100)
    lista_randomica.append(numero)
    somatorio += numero
    multiplicacao *= numero

print(f"A lista randomica é: {lista_randomica}")
print(f"A soma dos números é: {somatorio}")
print(f"A multiplicação dos números é: {multiplicacao}")
