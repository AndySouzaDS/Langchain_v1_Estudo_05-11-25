# 🐛 Debug Challenge 3

# **O que está errado?

#%%
from langchain_tavily import TavilySearch

search = TavilySearch()
results = search.invoke("Python")

print(results[0]['title'])

#%%
### 💡 Ver Solução

# Erros:

# 1. Faltou especificar `max_results`
# 2. `results` é um dict, não uma lista. Deveria ser `results['results'][0]['title']`

# Correto:

from langchain_tavily import TavilySearch

search = TavilySearch(max_results=2)
results = search.invoke("Python")

if results['results']:
    print(results['results'][0]['title'])
# %%
