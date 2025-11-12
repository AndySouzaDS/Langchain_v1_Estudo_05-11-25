from langchain_core.tools import tool
from datetime import datetime

@tool
def dias_ate_evento(data_evento: str) -> str:
    """Calcula quantos dias faltam até uma data. Formato: YYYY-MM-DD"""
    try:
        evento = datetime.strptime(data_evento, "%Y-%m-%d")
        hoje = datetime.now()
        diferenca = (evento - hoje).days

        if diferenca < 0:
            return f"Esse evento já passou há {abs(diferenca)} dias"
        elif diferenca == 0:
            return "O evento é hoje!"
        else:
            return f"Faltam {diferenca} dias para o evento."
    except:
        return "Formato de data inválido. Use YYYY-MM-DD"
    
# testar
resultado = dias_ate_evento.invoke({"data_evento": "2025-12-25"})
print(resultado)