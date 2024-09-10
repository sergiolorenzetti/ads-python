
#Função de média
def calcula_media(nota1,nota2):
    soma_media = nota1+nota2
    media_final = soma_media/2
    return media_final

#Função de arredondamento
def arredondar_media(media_aluno):
    return round(media_aluno,2)

#Laço de repetição While com Input de notas

nota1 = float(input("Informe a nota 1 de 0 a 10: "))
nota2 = float(input("Informe a nota 2 de 0 a 10: "))

#Verificar os valores antes de dar sequencia no processamento da nota e na saída de informações.
#Isso vai evitar saídas erradas e falhas durante o processamento.
#Vai ser necessário fazer um loop de while com opcão de "Saída"

#Verificar se imput é um número negativo

#Verificar se input é uma string, caso não for números retornar erro.

#Verificar a média não é negativa, caso for negativa retornar erro.

#Verificar se input é >10, caso fora do range retornar erro.

#Calcula média do aluno
media_aluno=calcula_media(nota1,nota2)

#Calcula conceito do aluno
if media_aluno >= 9 and media_aluno <= 10:
    conceito = 'A'
elif media_aluno >= 7.5 and media_aluno <= 8.9:
    conceito = 'B'
elif media_aluno >= 6 and media_aluno <= 7.4:
    conceito = 'C'
elif media_aluno >= 4 and media_aluno <= 5.9:
    conceito = 'D'
else:
    conceito = 'E'

#Classificação Aprovado e Reprovado

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    mensagem = "Aprovado"
else:
    mensagem = "Reprovado"

#Mostrar as notas, a média, o conceito e se o aluno foi aprovado ou reprovado.

print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Media: {media_aluno}")
print(f"Conceito: {conceito}")
print(f"{mensagem}")