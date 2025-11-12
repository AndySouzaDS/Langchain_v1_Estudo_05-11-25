from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

# modelo maior (mais capaz)
modelo_70b = init_chat_model(model="llama-3.3-70b-versatile", model_provider='groq')

# modelo menor (mais rápido)
modelo_8b = init_chat_model(model="llama-3.1-8b-instant", model_provider='groq')

query = "Explique IA em uma frase."

print("70B: ", modelo_70b.invoke([{"role": "user", "content": query}]).content)
print("8B: ", modelo_8b.invoke([{"role": "user", "content": query}]).content)
