#Entrada de valor de salário
salario_colaborador = float(input("Informe seu salário: "))

#Range de % de desconto
if salario_colaborador >0 and salario_colaborador<= 280.00:
    percentual_aumento=20
elif salario_colaborador >280.00 and salario_colaborador <= 700.00:
    percentual_aumento=15
elif salario_colaborador >700.00 and salario_colaborador <= 1500.00:
    percentual_aumento=10
elif salario_colaborador >1500.00:
    percentual_aumento=5
else:
    percentual_aumento=0

#Calcula aumento de salário
valor_aumento=salario_colaborador*(percentual_aumento/100)

#Calcula salário reajustado
salario_reajustado=valor_aumento+salario_colaborador

print(f"Salario antes do reajuste: R$ {salario_colaborador}")
print(f"O percentual do reajuste é: {percentual_aumento}%")
print(f"O valor do aumento é: R$ {valor_aumento}")
print(f"Salario depois do reajuste: R$ {salario_reajustado}")