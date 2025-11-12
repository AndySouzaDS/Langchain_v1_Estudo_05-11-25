import os
from dotenv import load_dotenv

# originalmente o código não tinha a chamada das credenciais no .env, as api keys não seriam validadas
load_dotenv()

def validate_setup():
    """Valida se todas as dependências estão instaladas e configuradas"""

    # checar imports
    try:
        import langchain
        import langgraph
        from langchain_groq import ChatGroq
        from langchain_tavily import TavilySearch
        print("✅ Todas as bibliotecas instaladas")
    except:
        print(f"❌ Erro de importação: {e}")
        return False
    
    # Essa checagem é deficiente, pois não testa individualmente cada API Key
    # checar api keys (é esperada as 2 api keys)
    if not os.getenv("GROQ_API_KEYw"):
        print("❌ GROQ_API_KEY não configurada!")
        return False
    
    if not os.getenv("TAVILY_API_KEYy"):
        print("❌ TAVILY_API_KEY não configurada!")
        return False
    
    print("✅ API Keys configuradas!")
    return True

# chamada da função (testa o setup)
validate_setup()
