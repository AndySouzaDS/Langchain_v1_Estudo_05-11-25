# 🔄 Variação 1 - Usando arquivo .env
from dotenv import load_dotenv
import os

# Criar arquivo .env com:
# GROQ_API_KEY=sua_key_aqui
# TAVILY_API_KEY=sua_key_aqui

load_dotenv()

# verificação de carregamento de credenciais
# este método é o ideal para esse contexto, pois informa se a variável foi encontrada ou não, porém ela não atribui o valor a uma variável para que um llm seja chamada
if os.getenv("GROQ_API_KEY"):
    print("✅ Groq API Key carregada!")
else:
    print("❌ Groq API Key não encontrada!")


# # Método de teste de API Key 2
# # esta forma não é ideal, pois mostraria o api key inteiro, ou a mensagem de erro parcial
# groq_api_key = os.environ.get("GROQ_API_KEY", "API_KEY não encontrada!")
# print(groq_api_key[:8])
