# Define a nota do aluno
nota = 8.5

# Verifica o conceito baseado na nota
if nota >= 9:
    conceito = "A"
elif nota >= 7 and nota < 9:
    conceito = "B"
elif nota >= 5:
    conceito = "C"
else:
    conceito = "D"

# Exibe o conceito
print("Conceito:", conceito)
