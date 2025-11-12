from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

# criar modelo usando string notation
model = init_chat_model("llama-3.3-70b-versatile", model_provider='groq')

# enviar mensagem simples
query = "Oi! Tudo bem com você?"
response = model.invoke([{"role": "user", "content": query}])

# acessar resposta
print(response.content)


# Pontos importantes:

# .invoke() recebe uma lista de mensagens
# Cada mensagem é um dict com role e content
# .content extrai o texto da resposta