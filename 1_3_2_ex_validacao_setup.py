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
    
    # checar api keys (é esperada as 2 api keys)
    if os.getenv("GROQ_API_KEYq"):
        print('✅ Groq API Key carregada!')
    else:
        print("❌ GROQ_API_KEY não configurada!")
        return False
    
    if os.getenv("TAVILY_API_KEYi"):
        print('✅ TAVILY API Key carregada!')
    else:
        print("❌ TAVILY_API_KEY não configurada!")
        return False
    
    if "GROQ_API_KEY" and "TAVILY_API_KEY":
        print("✅ API Keys configuradas")

# chamada da função (testa o setup)
validate_setup()
