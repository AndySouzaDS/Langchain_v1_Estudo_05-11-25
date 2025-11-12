# 🐛 Debug Challenge 2
# O que está errado neste código?

from langchain.chat_models import init_chat_model
 
model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

# Erro: .invoke() espera uma lista de mensagens, não uma string.
# response = model.invoke("Hi!")

response = model.invoke([{"role": "user", "content": "Hi!"}])
print(response.content)

# ✅ Checklist de Domínio
# Você consegue sem olhar a apostila:

# Criar um chat model com init_chat_model()?
# Enviar uma mensagem com .invoke()?
# Adicionar um system message?
# Acessar a resposta com .content?
