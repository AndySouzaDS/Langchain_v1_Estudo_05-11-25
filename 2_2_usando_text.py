from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("llama-3.3-70b-versatile", model_provider='groq')

query = "Em um paragráfo, o que é rag?"

response = model.invoke([{"role": "user", "content": query}])

# duas formas de acessar o texto
# print(f"Usando o '.text()' {response.text()}")  # método alternativo (obsoleto)
print(f"Usando o '.content': {response.content}\n")


