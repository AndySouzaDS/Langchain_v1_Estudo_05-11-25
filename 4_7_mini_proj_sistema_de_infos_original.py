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

# 1.2. Uma função que lista todas as tools disponíveis
from langchain_core.tools import BaseTool
from typing import List

# criação da lista de tools
tools = [info_pais, calcular_idade, converter_moeda]

def listar_tools(tools_list: List[BaseTool]) -> None:
    """Lista todas as tools disponíveis."""
    print("\n📋 Tools disponíveis:")
    for i, tool in enumerate(tools_list, 1):
        print(f"{i}. {tool.name}")
        print(f" {tool.description}\n")

# 1.3. Um menu interativo que permite testar cada tool
def menu():
    while True:
        print("\n" + "="*50)
        print("🤖 SISTEMA DE INFORMAÇÕES")
        print("="*50)
        print("1 - Listar tools")
        print("2 - Testar info_pais")
        print("3 - Testar calcular_idade")
        print("4 - Testar converter_moeda")
        print("0 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "0":
            print("👋 Até logo!")
            break
        elif opcao == "1":
            listar_tools(tools)
        elif opcao == "2":
            pais = input("Digite o país: ")
            print(info_pais.invoke({"pais": pais}))
        elif opcao == "3":
            ano = int(input("Ano de nascimento (Ex.: 1990): "))
            print(calcular_idade.invoke({"ano_nascimento": ano}))
        elif opcao == "4":
            valor = float(input("Valor: "))
            de = input("BRL/USD/EUR: ")
            para = input("Para (BRL/USD/EUR): ")
            print(converter_moeda.invoke({"valor": valor, "de": de, "para": para}))

# executar
menu()


# if __name__ == "__main__":
#     # response = calcular_idade.invoke({"ano_nascimento": 1975})
#     # print(response)
#     response = converter_moeda.invoke({"valor": 100, "de": "brl", "para": "usd"})
#     print(response)

