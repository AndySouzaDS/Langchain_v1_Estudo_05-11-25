# # 🐛 Debug Challenge 4

# # **O que está errado?
# from langchain_core.tools import tool

# @tool
# def calcular(x, y):
#     return x + y

# result = calcular.invoke({"x": 5, "y": 3})
# print(result)

# Erros:

# 1. Falta importar pacote para receber variáveis de ambiente
# 2. Falta instanciar o pacote para receber variáveis de ambiente
# 3. Faltam type hints nos parâmetros (obrigatório!)
# 4. Falta docstring (o LLM não saberá quando usar!)
# 5. Falta type hint de retorno (recomendado)

# Correto:
from langchain_core.tools import tool

@tool
def calcular(x: float, y: float) -> float:
    """Soma dois números."""
    return x + y

result = calcular.invoke({"x": 5, "y": 3})
print(result)

# ✅ Checklist de Domínio

# Você consegue sem olhar a apostila:

# - [ ] Criar uma tool com `@tool`?
# - [ ] Adicionar type hints corretos?
# - [ ] Escrever uma docstring clara?
# - [ ] Testar a tool com `.invoke()`?
# - [ ] Criar uma lista de múltiplas tools?