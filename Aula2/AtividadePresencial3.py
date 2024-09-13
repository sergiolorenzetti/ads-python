numeros_inteiros = []
numeros_pares = []
numeros_impares = []

for i in range(10):
    numeros_digitados = int(input(f"Digite o número {i+1}: "))
    numeros_inteiros.append(numeros_digitados)

    if numeros_digitados % 2 == 0:
        numeros_pares.append(numeros_digitados)
    else:
        numeros_impares.append(numeros_digitados)

print(f"A lista de numeros digitados foi: {numeros_inteiros}")
print(f"A lista de numeros pares é: {numeros_pares}")
print(f"A lista de numeros impares é: {numeros_impares}")
print(f"O numero na posição 2 é: {numeros_inteiros[2]}")