# 1. Instalar dependências (no terminal)
# pip install langchain langgraph langchain-groq langchain-tavily

# 2. Configurar API Keys
import os
import getpass
# from dotenv import load_dotenv

# # importando das variáveis de ambiente as API Keys
# load_dotenv()

# # se a API Key da Groq não estiver na memória, deverá ser digitada
if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter Groq API Key: ")


# tavily api key (para busca)
if not os.environ.get("TAVILY_API_KEY"):
    os.environ["TAVILY_API_KEY"] = getpass.getpass("Enter Tavily API Key: ")

# Nota: qualquer valores digitados não passaram por validação e serão aceitos
print("✅ Setup completo!")
