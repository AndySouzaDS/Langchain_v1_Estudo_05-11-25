# 💪 Exercício Desafio 4

# Crie 3 tools para um "assistente pessoal":

# 1. `contar_palavras(texto: str)` - conta palavras em um texto
# 2. `inverter_texto(texto: str)` - inverte um texto
# 3. `eh_palindromo(texto: str)` - verifica se é palíndromo

# Agrupe as 3 em uma lista chamada `tools_texto`.

from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool
def contar_palavras(texto: str) -> str:
    """Conta o número de palavras em um texto."""
    palavras = len(texto.split())
    return f"O texto tem {palavras} palavras."

@tool
def inverter_texto(texto: str) -> str:
    """Inverter um texto (de trás para frente)."""
    return texto[::-1]

@tool
def eh_palindromo(texto: str) -> str:
    """Verifica se um texto é palíndromo (igual de trás para frente)."""
    texto_limpo = texto.lower().replace(" ", "")
    if texto_limpo == texto_limpo[::-1]:
        return f"'{texto}' É um palíndromo!"
    else:
        return f"'{texto}' Não é um palíndromo!"
    
# agrupar
tools_texto = [contar_palavras, inverter_texto, eh_palindromo]

# testar
print(contar_palavras.invoke({"texto": "Python é incrível."}))
print(inverter_texto.invoke({"texto": "LangChain"}))
print(eh_palindromo.invoke({"texto": "arara"}))
