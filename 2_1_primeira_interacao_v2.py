from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

# criando um modelo usando string notation
model = init_chat_model(model="llama-3.3-70b-versatile", model_provider="groq")

# enviando mensagem simples
query = "Olá"
response = model.invoke([{"role": "user", "content": query}])

# acessar a resposta
print(response.content)
