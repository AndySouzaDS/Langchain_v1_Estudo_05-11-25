from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

# criar múltiplas tools
search = TavilySearch(max_results=2)
search_news = TavilySearch(max_results=5)  # mais resultados para notícias

# lista de tools (usada por agentes)
tools = [search, search_news]

print(f"Total de tools: {len(tools)}")
print(f"Tools disponível: {tools[0].__class__.__name__}")
