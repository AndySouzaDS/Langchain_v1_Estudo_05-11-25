# CONCEITO 2: Chat Models com init_chat_model

## 📖 Teoria

No LangChain v1.0.0, usamos `init_chat_model()` para criar modelos de forma **provider-agnostic**. 

Isso significa que você pode trocar de **provider** (OpenAI, Anthropic, Groq) mudando apenas uma string.

Sintaxe: `init_chat_model("provider:model-name")`

Para Groq: `groq:llama-3.3-70b-versatile` ou apenas o nome do modelo se já configurado.
