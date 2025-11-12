
#%%
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

#%%
# criar a tool de busca
search = TavilySearch(max_results=2)

#%%
# executar busca diretamente
search_results = search.invoke("Como está o tempo em Floripa?")

print(search_results)

#%%
type(search_results)


#%%
search_results.keys()

#%%
respostas = search_results['results']
print(respostas)

#%%
type(respostas)

#%%
respostas[0].keys()

#%%
for r in respostas:
    link = r['url']
    titulo = r['title']
    conteudo = r['content']
    score = r['score']
    print(
        f"Link: {link}\nTítulo: {titulo}\nConteúdo: {conteudo}\nScore: {score}\n\n"
    )

# %%
