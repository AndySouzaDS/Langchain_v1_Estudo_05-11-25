# 📝 Exercício Guiado 4

# Objetivo: Criar uma tool de conversão de temperatura

# Passo 1: Crie uma tool que converte Celsius para Fahrenheit

# Passo 2: Docstring deve explicar o que a tool faz

# Passo 3: Teste com alguns valores
from langchain_core.tools import tool

@tool
def celsius_para_fahrenheit(celsius: float) -> str:
    """Converte temperatura de Celsius para Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}ºC = {fahrenheit}ºF"


# testar
print(celsius_para_fahrenheit.invoke({"celsius": 0}))    # 32°F
print(celsius_para_fahrenheit.invoke({"celsius": 100}))  # 212°F
print(celsius_para_fahrenheit.invoke({"celsius": 25}))   # 77°F
