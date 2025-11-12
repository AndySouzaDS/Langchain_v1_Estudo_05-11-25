# Exercício Desafio 3

# Crie uma função `buscar_e_resumir(query)` que:

# 1. Faz uma busca no Tavily
# 2. Usa o LLM para resumir o conteúdo do primeiro resultado
# 3. Retorna o resumo

#%%
from langchain_tavily import TavilySearch
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

def buscar_resumir(query):

    # busca
    search = TavilySearch(max_results=1)
    results = search.invoke(query)

    # tratamento de erros
    if not results['results']:
        return "Nenhum resultado encontrado."

    # extração de conteúdo
    conteudo = results['results'][0]['content']

    # resumir com LLM
    model = init_chat_model(model="llama-3.3-70b-versatile", model_provider="groq")
    messages = [
        {"role": "system", "content": "Resuma o texto a seguir em 2 frases."},
        {"role": "user", "content": conteudo}
    ]

    resumo = model.invoke(messages).content
    return resumo

# testar
resultado = buscar_resumir("LangChain framework")



#%%
print(resultado)

