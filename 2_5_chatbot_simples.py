from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(model="llama-3.3-70b-versatile", model_provider="groq")

pergunta = str(input("Por favor digite sua pergunta: "))

response = model.invoke([{"role": "user", "content": pergunta}])
print(f"Resposta:\n{response.content}")
