from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

# modelo maior (maior capacidade)
model_70b = init_chat_model(model="llama-3.3-70b-versatile", model_provider="groq")

# modelo menor (mais rápido)
model_8b = init_chat_model(model="llama-3.1-8b-instant", model_provider="groq")

query = "O que é MCP no contexto de LLM, desenvolvido pela Claude AI, em uma frase."

print(f'70B: {model_70b.invoke([{"role": "user", "content": query}]).content}')
print(f'8B: {model_8b.invoke([{"role": "user", "content": query}]).content}')
