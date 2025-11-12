# %%
# 🔄 Variação 1 - Acessando Resultados
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

search = TavilySearch(max_results=2)
results = search.invoke("Qual a capital do Brasil?")

# %%
# acessar partes específicas
print("Query:", results['query'])
print("\nResultados encontrados:", len(results['results']))

resultado = results['results']

for i, result in enumerate(resultado, 1):
    print(f"\n--- Resultado {i} ---")
    print("Título:", result['title'])
    print("URL:", result['url'])
    print("Conteúdo:", result['content'])
    print("Score:", result['score'])


# %%
