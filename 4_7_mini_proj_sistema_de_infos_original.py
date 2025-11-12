from langchain_core.tools import tool


# 1. 3 tools customizadas (você escolhe o tema)
@tool
def info_pais(pais: str) -> str:
    """Retorna informações básicas sobre um país."""
    paises = {
        "brasil": "Capital: Brasília, População: 214M, Idioma: Português",
        "eua": "Capital: Washington DC, População: 350M, Idioma: Inglês",
        "japao": "Capital: Tóquio, População: 125M, Idioma: Japonês"
    }
    return paises.get(pais.lower(), "País não encontrado no banco de dados")

@tool
def calcular_idade(ano_nascimento: int) -> str:
    """Calcula a idade baseada no ano de nascimento. Ano de Nascimento formato: YYYY"""
    from datetime import datetime
    idade = datetime.now().year - ano_nascimento
    return f"Você tem aproximadamente {idade} anos."

@tool
def converter_moeda(valor: float, de: str, para: str) -> str:
    """Converter valores entre moedas (BRL, USD, EUR)"""
    taxas = {
        ("brl", "usd"): 0.20,
        ("usd", "brl"): 5.00,
        ("brl", "eur"): 0.18,
        ("eur", "brl"): 5.50
    }

    chave = (de.lower(), para.lower())
    if chave in taxas:
        resultado = valor * taxas[chave]
        return f"{valor:.2f} {de.upper()} = {resultado:.2f} {para.upper()}"
    return "Conversão não disponível."

tools = [info_pais, calcular_idade, converter_moeda]





if __name__ == "__main__":
    # response = calcular_idade.invoke({"ano_nascimento": 1975})
    # print(response)
    response = converter_moeda.invoke({"valor": 100, "de": "brl", "para": "usd"})
    print(response)

