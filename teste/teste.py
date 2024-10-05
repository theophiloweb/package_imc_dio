from pacote_imc import IMC

# Teste com diferentes categorias de peso
testes = [
    (50, 1.70),    # Abaixo do peso
    (70, 1.75),    # Peso normal
    (85, 1.75),    # Sobrepeso
    (100, 1.75),   # Obesidade grau 1
]

for peso, altura in testes:
    resultado = IMC.calcular_imc(peso, altura)
    print(f"Peso: {peso}kg, Altura: {altura}m")
    print(resultado)
    print("-" * 30)