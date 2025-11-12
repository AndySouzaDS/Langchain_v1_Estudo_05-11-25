# 💪 Exercício Desafio 1
# Crie uma função test_connection() que:
# Tenta criar um modelo Groq
# Tenta criar uma TavilySearch
# Retorna True se ambos funcionarem, False caso contráriog

from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

def test_connection():
    """Testa a com conexão com Groq e Tavily."""
    try:
       # Testar Groq
       model = ChatGroq(model="llama-3.3-70b-versatile")
       print("✅ Groq conectado") 

       # Testar Tavily
       search = TavilySearch(max_results=1)
       print("✅ Tavily conectado")

       return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False
    
test_connection()
