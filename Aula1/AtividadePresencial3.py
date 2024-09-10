# Input de três números
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

# Função que recebe os números e retorna a soma
def soma_tres_numeros(num1, num2, num3):
    return num1 + num2 + num3

# Chama a função para calcular a soma e armazena o resultado
resultado_soma = soma_tres_numeros(num1, num2, num3)

# Exibe o resultado
print(f"A soma dos três números é: {resultado_soma}")