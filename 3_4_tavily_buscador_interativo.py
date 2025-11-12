#%%
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

# tool
search = TavilySearch(max_results=2)

# busca interativa
query = input("O que você quer buscar? ")

# pesquisar
response = search.invoke(query)

# resultado
print(type(response))

# %%
response.keys()

# %%
# resultado da 1ª resposta
respostas = response['results'][0]

# %%
for chave, valor in respostas.items():
    if chave == 'title':
        print(f"Título: {valor}")
        
    if chave == 'url':
        print(f"URL: {valor}")
    

# %%
for x in respostas.values():
    print(x)


# %%
