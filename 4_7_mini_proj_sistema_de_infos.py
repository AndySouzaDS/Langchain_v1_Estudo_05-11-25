# 🚀 MINI-PROJETO 1: Sistema de Informações

# Objetivo: Integrar tudo que aprendeu até agora

# Crie um sistema com:

# 1. 3 tools customizadas (você escolhe o tema)
# 2. Uma função que lista todas as tools disponíveis
# 3. Um menu interativo que permite testar cada tool

#%%
from langchain_tavily import TavilySearch, TavilyExtract
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()

#%%
# construção das tools
# 1. pesquisa de notícias
search = TavilySearch(max_results=1)
query = input("Qual a pesquisa desejada: ")
query_pt = f"Responda em português do Brasil a seguinte pergunta, em um paragráfo: {query}"
response = search.invoke(query_pt)['results']
resposta = response[0]['content']
print(resposta)

#%%
# documentação tavily extract
# https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/tools/tavily_extract.mdx
# https://docs.tavily.com/documentation/api-reference/endpoint/extract
# https://github.com/langchain-ai/docs/blob/main/src/oss/python/integrations/tools/tavily_extract.mdx

# 2. extraír conteúdos de páginas web
url_extract = input("Digite a url, que deseja extrai: ")
page_extract = TavilyExtract()
response = page_extract.invoke({"urls": [url_extract], "extract_depth": "advanced"})
respostas = response['results'][0]['raw_content']
print(respostas)

#%%
# 3. calcula descontos de preços de produtos
from langchain_core.tools import tool

@tool
def calcular_desconto(preco_produto: float, valor_desconto: float) -> float:
    """A partir do preço de um produto e um valor de desconto, retorna o valor de desconto e o preço final do produto em em reais."""
    try:
        if preco_produto > 0:
            preco_produto
        else:
            print("Erro: O preço do produto tem que ser maior do que R$ 0")
        
        if valor_desconto >= 0:
            if valor_desconto == 0:
                valor_desconto = 1
            else:
                print("Erro: O valor de desconto tem que ser maior do que 0")

            valor_desconto_reais = preco_produto * valor_desconto
            preco_final_produto = (preco_produto) - (preco_produto * valor_desconto)
            return valor_desconto_reais, preco_final_produto        
    except:
        return "Preencha os valores corretamente!"

#%%
response = calcular_desconto(100, 10)
print(response)

# %%
