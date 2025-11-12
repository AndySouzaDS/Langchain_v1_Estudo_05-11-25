from langchain_core.tools import tool

@tool
def calcular_imc(peso: float, altura: float) -> str:
    """Calcular o IMC  (Índice de Massa Corporal) dado peso em kg e altura em metros."""
    imc = peso / (altura ** 2)

    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"

    return f"IMC: {imc:.2f} - {categoria}"

resultado = calcular_imc.invoke({"peso": 72, "altura": 1.70})

# testar
print(resultado)
