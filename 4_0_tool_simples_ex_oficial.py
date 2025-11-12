from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Obter a previsão do tempo para uma determinada localização."""

    # simulação (em produção, chamaria a API real)
    return f"Está sempre ensolarado em {location}!"

# testar a tool diretamente
result = get_weather.invoke("São Paulo")
print(result)

# Simulação de Saída
# Está sempre ensolarado em São Paulo

# **Importante:** A docstring é CRUCIAL - o LLM decide usar a tool baseado nela!
