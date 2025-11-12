# CONCEITO 3: Tools - TavilySearch

## 📖 Teoria

Tools são funções que o LLM pode chamar para executar ações. No LangChain v1.0.0, tools são objetos com:

- Nome - identificador da tool
- Descrição - o que ela faz (o LLM lê isso!)
- Função - código executado

> **TavilySearch** é uma tool de busca na web pré-construída.

### 💻 Exemplo Oficial - Usando TavilySearch

```python
from langchain_tavily import TavilySearch
 
# Criar a tool de busca
search = TavilySearch(max_results=2)
 
# Executar busca diretamente
search_results = search.invoke("What is the weather in SF")
 
print(search_results)
# Retorna: dict com 'query', 'results', etc
```

#### Estrutura do resultado:

```bash
{
    'query': 'What is the weather in SF',
    'results': [
        {
            'title': '...',
            'url': '...',
            'content': '...',
            'score': 0.95
        }
    ]
}
```
