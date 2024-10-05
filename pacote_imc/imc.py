class IMC:
    @staticmethod
    def calcular_imc(peso: float, altura: float) -> str:
        # Calcula o IMC usando a fórmula: peso / (altura ^ 2)
        imc = peso / (altura ** 2)
        
        # Define a categoria do IMC baseado no valor calculado
        if imc < 18.5:
            categoria = "Abaixo do peso"
        elif 18.5 <= imc < 25:
            categoria = "Peso normal"
        elif 25 <= imc < 30:
            categoria = "Sobrepeso"
        elif 30 <= imc < 35:
            categoria = "Obesidade grau 1"
        elif 35 <= imc < 40:
            categoria = "Obesidade grau 2"
        else:
            categoria = "Obesidade grau 3"
        
        # Retorna uma string formatada com o IMC e a categoria
        return f"Seu IMC é {imc:.2f} - Classificação: {categoria}"