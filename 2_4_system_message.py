from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(model="llama-3.3-70b-versatile", model_provider="groq")

# lista de mensagens
messages = [
    {"role": "system", "content": "Você é um assistente que fala como um pirata."},
    {"role": "user", "content": "Olá, como vai?"}
]

response = model.invoke(messages)
print(response.content)
