## ChatGPT

Ótima pergunta — e bem no estilo da **arquitetura modular do LangChain v1.0**. 💡

No caso da `TavilySearch` (ou qualquer outra *Tool* no padrão LangChain), o parâmetro de idioma não é nativo da tool em si — ela só retorna o conteúdo bruto da API Tavily.
Mas existem **3 maneiras elegantes** de garantir que o **retorno final esteja em português (pt-BR)**, dependendo de onde você quer intervir no fluxo.

---

## 🧠 1. Traduzindo o retorno com uma *Tool Wrapper* (melhor prática LangChain v1)

Você pode criar uma *tool wrapper* que executa a TavilySearch, depois traduz o resultado automaticamente.

```python
from langchain_tavily import TavilySearch
from langchain_core.tools import tool
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

# modelo para tradução
translator = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# tool original
search = TavilySearch(max_results=1)

@tool
def search_pt(query: str) -> str:
    """Faz uma pesquisa na web e retorna o resultado em português (pt-BR)."""
    result = search.invoke(query)
    translation_prompt = f"Traduza o texto a seguir para português do Brasil, mantendo o sentido original:\n\n{result}"
    translated = translator.invoke([HumanMessage(content=translation_prompt)])
    return translated.content

# Exemplo de uso
if __name__ == "__main__":
    query = input("Qual a pesquisa desejada: ")
    response = search_pt.invoke(query)
    print("\n🔎 Resultado em português:\n")
    print(response)
```

🟢 **Vantagem:**
Funciona com qualquer retorno (mesmo inglês, chinês etc.), respeitando o estilo LangChain v1.0.

---

## ⚙️ 2. Passando a instrução de idioma diretamente na *query*

A Tavily tenta entender o idioma da consulta, então você pode direcionar a busca em português:

```python
query = input("Qual a pesquisa desejada: ")
query_pt = f"Responda em português: {query}"
response = search.invoke(query_pt)
print(response)
```

🟡 **Limitação:**
Nem sempre garante que o resultado será traduzido, pois depende da origem do conteúdo encontrado.

---

## 🔄 3. Traduzindo via pipeline pós-processamento (sem LLM)

Se quiser evitar usar tokens de um modelo para tradução, dá pra integrar uma lib como `deep_translator`:

```python
from langchain_tavily import TavilySearch
from deep_translator import GoogleTranslator

search = TavilySearch(max_results=1)
query = input("Qual a pesquisa desejada: ")
response = search.invoke(query)

# tradução automática
traduzido = GoogleTranslator(source='auto', target='pt').translate(response)
print(traduzido)
```

🟢 **Vantagem:**
Zero custo de API da OpenAI.
🔴 **Desvantagem:**
Tradução menos contextual, mais literal.

---

## 🚀 Conclusão

| Método                                | Solução                        | Melhor para             |
| ------------------------------------- | ------------------------------ | ----------------------- |
| 1️⃣ Wrapper com ChatOpenAI            | Resultado contextual e natural | Aplicações RAG, agentes |
| 2️⃣ Query com “Responda em português” | Simples, rápido                | Testes, protótipos      |
| 3️⃣ Pós-processamento com tradutor    | Custo zero, fácil              | Ferramentas autônomas   |

---

Se quiser, posso te mostrar **como integrar essa `search_pt` como uma `Tool` compatível com um agente LangChain v1**, para que ele use automaticamente resultados em português durante o raciocínio. Deseja que eu monte esse exemplo?
