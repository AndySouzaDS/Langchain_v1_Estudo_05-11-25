#%%
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

search = TavilySearch(max_results=2)

try:
    results = search.invoke("Notícias IA Verticais.")
    noticias = results

    if results['results']:
        print("✅ Busca bem-sucedida!")
        print(f"Encontramos {len(results['results'])} resultados.")
        print(noticias)
        
    else:
        print("⚠️ Nenhum resultado encontrado.")

except Exception as e:
    print(f"❌ Erro na busca: {e}")

#%%
print(type(results))
print(noticias.keys())
print(noticias['content'])

#%%
for noticia in noticias.items():
    print(noticia['content'])


# %%
for chave, valor in noticias.items():
    if chave == "content":
        print(valor)

# %%
