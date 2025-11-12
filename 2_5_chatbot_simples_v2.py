from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(model="llama-3.3-70b-versatile", model_provider="groq")

nome = input("Seu nome: ")
idade = input("Sua idade: ")

messages = [
    {"role": "system", "content": "Você é um assistente amigável, que personaliza respostas."},
    {"role": "user", "content": f"Meu nome é {nome} e tenho {idade} anos. Me dê uma sugestão de hobby."}
]

response = model.invoke(messages)
print(f"\n🤖 {response.content}")
