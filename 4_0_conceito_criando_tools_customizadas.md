# **CONCEITO 4: Criando Tools Customizadas**

## 📖 **Teoria**

Você pode criar suas próprias tools usando o decorator `@tool`

### **Requisitos:**

1. **Docstring** - O LLM lê isso para saber quando usar a tool.
2. **Type hints** - Obrigatórios para os parâmetros.
3. **Return type** - Recomendado para clareza.

Formato:

```python
@tool
def nome_da_tool(parametro: tipo) -> tipo_retorno:
    """Descrição que o LLM lê"""
    # código
    return resultado
```

## 💻 **Exemplo Oficial - Tool Simples**

```python
from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Get weather for a given location."""
    # Simulação (em produção, chamaria API real)
    return f"It's always sunny in {location}!"

# Testar a tool diretamente
result = get_weather.invoke("São Paulo")
print(result)
# Saída: It's always sunny in São Paulo!
```

### **Importante:** 

A docstring é CRUCIAL - o LLM decide usar a tool baseado nela.