# Projeto IMC

Um pacote Python simples para calculo do Indice de Massa Corporal (IMC).

## Instalacao

Voce pode instalar o pacote usando pip:

```
pip install -i https://test.pypi.org/simple/ projeto-imc
```

## Como usar

```python
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
```

## Requisitos

- Python 3.10 ou superior

## Autor

Teophilo Silva

## Licenca

Este projeto esta sob a licenca MIT.

## Objetivo

Este pacote foi criado como parte do curso de Engenharia de Dados com Python da DIO em parceria com a NTT DATA.
