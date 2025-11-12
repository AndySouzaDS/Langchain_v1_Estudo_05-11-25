from langchain_core.tools import tool

@tool
def somar(a: float, b: float) -> float:
    """Somar dois números."""
    return a + b

@tool
def multiplicar(a: float, b: float) -> float:
    """Multiplicar dois números"""
    return a * b

@tool
def dividir(a: float, b: float) -> str:
    """Dividir dois números"""
    if b == 0:
        return "Erro: Divisão por zero!"
    return f"{a / b}"

# agrupar tools
tools_matematica = [somar, multiplicar, dividir]

print(f"Tools disponíveis: {len(tools_matematica)}")

for tool in tools_matematica:
    print(f"- {tool.name}: {tool.description}")
