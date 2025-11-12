Componentes principais

# **Tools**

Muitas aplicações de IA interagem com os usuários por meio de linguagem natural. 

No entanto, alguns casos de uso exigem que os modelos interajam diretamente com **sistemas externos — como APIs, bancos de dados ou sistemas de arquivos** — usando entradas estruturadas.

> As tools são componentes que [os agentes](https://docs.langchain.com/oss/python/langchain/agents) chamam para executar ações.

Elas ampliam as capacidades do modelo, permitindo que ele interaja com o mundo por meio de entradas e saídas bem definidas.

> As tools encapsulam uma função invocável e seu esquema de entrada.

Esses elementos podem ser passados para [modelos de chat](https://docs.langchain.com/oss/python/langchain/models) compatíveis, permitindo que o modelo decida se deve invocar uma tool e com quais argumentos.

Nesses cenários, a chamada de tools permite que os modelos gerem solicitações que estejam em conformidade com um esquema de entrada especificado.

📌 **Uso de tools do lado do servidor**

Alguns modelos de chat (por exemplo, [OpenAI](https://docs.langchain.com/oss/python/integrations/chat/openai) , [Anthropic](https://docs.langchain.com/oss/python/integrations/chat/anthropic) e [Gemini](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai) ) possuem [tools integradas](https://docs.langchain.com/oss/python/langchain/models#server-side-tool-use) que são executadas no servidor, como mecanismos de busca na web e interpretadores de código. Consulte a [visão geral do provedor](https://docs.langchain.com/oss/python/integrations/providers/overview) para saber como acessar essas tools com o seu modelo de chat específico.

### 📚 Definição básica da ferramenta

A maneira mais simples de criar uma ferramenta é com o **decorador** [`@tool`](https://reference.langchain.com/python/langchain/tools/#langchain.tools.tool).

Por padrão, a **docstring da função se torna a descrição da ferramenta**, ajudando o modelo a entender quando usá-la:

```python
from langchain.tools import tool

@tool
def search_database(query: str, limit: int = 10) -> str:
    """Pesquise no banco de dados de clientes por registros que correspondam à consulta.

Args:
    query: Termos de pesquisa
    limit: Número máximo de resultados a serem retornados
    """
    return f"Encontre {limit} resultados para '{query}'"
```

As **dicas de tipo são necessárias**, pois definem o esquema de entrada da ferramenta.

**A docstring deve ser informativa e concisa para ajudar o modelo a entender a finalidade da ferramenta.**

### 📌 Personalizar propriedades da ferramenta

#### **✅ Nome da ferramenta personalizada**

Por padrão, **o nome da ferramenta deriva do nome da função**. Altere-o se precisar de algo mais descritivo:

```python
@tool("web_search")  # nome customizado
def search(query: str) -> str:
    """Busque na web por informações."""
    return f"Resultados para: {query}"

print(search.name)  # ferramementa pesquisa web
```

### **✅ Descrição de tools personalizada**

Substitua a descrição da ferramenta gerada automaticamente para obter orientações mais claras sobre o modelo:

```python
@tool("calculator", description="Realiza cálculos aritméticos. Use esta ferramenta para qualquer problema matemático.")
def calc(expression: str) -> str:
    """Avalia expressões matemáticas."""
    return str(eval(expression))
```

### ✅ Definição de esquema avançado

Defina entradas complexas com modelos Pydantic ou esquemas JSON:

#### **📌 Modelo Pydantic**

```python
from pydantic import BaseModel, Field
from typing import Literal

class WeatherInput(BaseModel):
    """Entrada para consultas meteorológicas."""
    location: str = Field(description="Nome da cidade ou coordenadas.")
    units: Literal["celsius", "fahrenheit"] = Field(
        default="celsius",
        description="Preferência de unidade de temperatura."
    )
    include_forecast: bool = Field(
        default=False,
        description="Include 5-day forecast"
    )

@tool(args_schema=WeatherInput)
def get_weather(location: str, units: str = "celsius", include_forecast: bool = False) -> str:
    """Veja as condições meteorológicas atuais e a previsão opcional."""
    temp = 22 if units == "celsius" else 72
    result = f"Condições meteorológicas atuais em {location}: {temp} graus {units[0].upper()}"
    if include_forecast:
        result += "\nPróximos 5 dias: Ensolarado"
    return result
```

#### **📌 Esquema JSON**

```python
weather_schema = {
    "type": "object",
    "properties": {
        "location": {"type": "string"},
        "units": {"type": "string"},
        "include_forecast": {"type": "boolean"}
    },
    "required": ["location", "units", "include_forecast"]
}

@tool(args_schema=weather_schema)
def get_weather(location: str, units: str = "celsius", include_forecast: bool = False) -> str:
    """Veja as condições meteorológicas atuais e a previsão opcional."""
    temp = 22 if units == "celsius" else 72
    result = f"Condições meteorológicas atuais em {location}: {temp} graus {units[0].upper()}"
    if include_forecast:
        result += "\nPróximos 5 dias: Ensolarado"
    return result
```

### 💡 Acessando o contexto

> **Por que isso é importante:**

As tools são mais poderosas quando podem acessar o estado do agente, o contexto de tempo de execução e a memória de longo prazo. Isso permite que as tools tomem decisões contextuais, personalizem respostas e mantenham informações ao longo das conversas.

O contexto de tempo de execução oferece uma maneira de injetar dependências (como conexões de banco de dados, IDs de usuário ou configurações) em suas tools em tempo de execução, tornando-as mais testáveis e reutilizáveis.

As tools podem acessar informações de tempo de execução por meio do parâmetro `ToolRuntime`, que fornece:

- **Estado** - Dados mutáveis que fluem durante a execução (ex.: mensagens, contadores, campos personalizados).

- **Contexto** - Configuração imutável, como IDs de usuário, detalhes da sessão ou configuração específica do aplicativo.

- **Armazenar** - Memória persistente de longo prazo entre conversas.

- **Stream Writer** - Transmita atualizações personalizadas à medida que as tools são executadas.
- **Configuração** - `RunnableConfig`para a execução.

- **ID da chamada da ferramenta** - ID da chamada da ferramenta atual.

### 📌 `ToolRuntime`

Utilize `ToolRuntime` para acessar todas as informações de tempo de execução em um único parâmetro. Basta adicioná-lo `runtime: ToolRuntime` à assinatura da sua ferramenta e ele será injetado automaticamente sem ser exposto ao LLM.

✅ **`ToolRuntime`**

Um parâmetro unificado que fornece às tools acesso ao estado, contexto, armazenamento, streaming, configuração e ID da chamada da ferramenta. 

Isso substitui o padrão antigo de [`InjectedState`](https://reference.langchain.com/python/langgraph/agents/#langgraph.prebuilt.tool_node.InjectedState) usar [`InjectedStore`](https://reference.langchain.com/python/langgraph/agents/#langgraph.prebuilt.tool_node.InjectedStore) anotações [`get_runtime`](https://reference.langchain.com/python/langgraph/runtime/#langgraph.runtime.get_runtime) separadas [`InjectedToolCallId`](https://reference.langchain.com/python/langchain/tools/#langchain.tools.InjectedToolCallId).

O ambiente de execução fornece automaticamente essas funcionalidades às suas funções de ferramenta, sem que você precise passá-las explicitamente ou usar estado global.

#### **Acessando o estado:** 

As tools podem acessar o estado atual do grafo usando `ToolRuntime`:

```python
from langchain.tools import tool, ToolRuntime

# Access the current conversation state
@tool
def summarize_conversation(
    runtime: ToolRuntime
) -> str:
    """Summarize the conversation so far."""
    messages = runtime.state["messages"]

    human_msgs = sum(1 for m in messages if m.__class__.__name__ == "HumanMessage")
    ai_msgs = sum(1 for m in messages if m.__class__.__name__ == "AIMessage")
    tool_msgs = sum(1 for m in messages if m.__class__.__name__ == "ToolMessage")

    return f"Conversation has {human_msgs} user messages, {ai_msgs} AI responses, and {tool_msgs} tool results"

# Access custom state fields
@tool
def get_user_preference(
    pref_name: str,
    runtime: ToolRuntime  # ToolRuntime parameter is not visible to the model
) -> str:
    """Get a user preference value."""
    preferences = runtime.state.get("user_preferences", {})
    return preferences.get(pref_name, "Not set")
```

O parâmetro `tool_runtime` está oculto no modelo. No exemplo acima, o modelo só vê o parâmetro `pref_name` no esquema da ferramenta — `tool_runtime` ele *não* está incluído na solicitação.

#### **Atualizando estado:** Utilize [`Command`](https://reference.langchain.com/python/langgraph/types/#langgraph.types.Command) para atualizar o estado do agente ou controlar o fluxo de execução do grafo:

```python
from langgraph.types import Command
from langchain.messages import RemoveMessage
from langgraph.graph.message import REMOVE_ALL_MESSAGES
from langchain.tools import tool, ToolRuntime

# Update the conversation history by removing all messages
@tool
def clear_conversation() -> Command:
    """Clear the conversation history."""

    return Command(
        update={
            "messages": [RemoveMessage(id=REMOVE_ALL_MESSAGES)],
        }
    )

# Update the user_name in the agent state
@tool
def update_user_name(
    new_name: str,
    runtime: ToolRuntime
) -> Command:
    """Update the user's name."""
    return Command(update={"user_name": new_name})
```

### Contexto

Acesse configurações imutáveis e dados contextuais, como IDs de usuário, detalhes da sessão ou configurações específicas do aplicativo por meio de `runtime.context`. As tools podem acessar o contexto de tempo de execução através de `ToolRuntime`:

```python
from dataclasses import dataclass
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime

USER_DATABASE = {
    "user123": {
        "name": "Alice Johnson",
        "account_type": "Premium",
        "balance": 5000,
        "email": "alice@example.com"
    },
    "user456": {
        "name": "Bob Smith",
        "account_type": "Standard",
        "balance": 1200,
        "email": "bob@example.com"
    }
}

@dataclass
class UserContext:
    user_id: str

@tool
def get_account_info(runtime: ToolRuntime[UserContext]) -> str:
    """Get the current user's account information."""
    user_id = runtime.context.user_id

    if user_id in USER_DATABASE:
        user = USER_DATABASE[user_id]
        return f"Account holder: {user['name']}\nType: {user['account_type']}\nBalance: ${user['balance']}"
    return "User not found"

model = ChatOpenAI(model="gpt-4o")
agent = create_agent(
    model,
    tools=[get_account_info],
    context_schema=UserContext,
    system_prompt="You are a financial assistant."
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's my current balance?"}]},
    context=UserContext(user_id="user123")
)
```

### Memória (Armazenamento)

Acesse dados persistentes entre conversas usando o repositório. O repositório é acessado via [inserir caminho aqui] `runtime.store`e permite salvar e recuperar dados específicos do usuário ou do aplicativo. As tools podem acessar e atualizar o armazenamento através de `ToolRuntime`:

```python
from typing import Any
from langgraph.store.memory import InMemoryStore
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime

# Access memory
@tool
def get_user_info(user_id: str, runtime: ToolRuntime) -> str:
    """Look up user info."""
    store = runtime.store
    user_info = store.get(("users",), user_id)
    return str(user_info.value) if user_info else "Unknown user"

# Update memory
@tool
def save_user_info(user_id: str, user_info: dict[str, Any], runtime: ToolRuntime) -> str:
    """Save user info."""
    store = runtime.store
    store.put(("users",), user_id, user_info)
    return "Successfully saved user info."

store = InMemoryStore()
agent = create_agent(
    model,
    tools=[get_user_info, save_user_info],
    store=store
)

# First session: save user info
agent.invoke({
    "messages": [{"role": "user", "content": "Save the following user: userid: abc123, name: Foo, age: 25, email: foo@langchain.dev"}]
})

# Second session: get user info
agent.invoke({
    "messages": [{"role": "user", "content": "Get user info for user with id 'abc123'"}]
})
# Here is the user info for user with ID "abc123":
# - Name: Foo
# - Age: 25
# - Email: foo@langchain.dev
```

Veja todas as 42 linhas

### Stream Writer

Transmita atualizações personalizadas de tools à medida que elas são executadas `runtime.stream_writer`. Isso é útil para fornecer feedback em tempo real aos usuários sobre o que uma ferramenta está fazendo.

```python
from langchain.tools import tool, ToolRuntime

@tool
def get_weather(city: str, runtime: ToolRuntime) -> str:
    """Get weather for a given city."""
    writer = runtime.stream_writer

    # Stream custom updates as the tool executes
    writer(f"Looking up data for city: {city}")
    writer(f"Acquired data for city: {city}")

    return f"It's always sunny in {city}!"
```

Se você usar `runtime.stream_writer`o LangGraph dentro da sua ferramenta, ela deverá ser invocada em um contexto de execução do LangGraph. Consulte [a seção Streaming](https://docs.langchain.com/oss/python/langchain/streaming) para obter mais detalhes.

---

[Edite o código-fonte desta página no GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/tools.mdx)

[Conecte esses documentos programaticamente](https://docs.langchain.com/use-these-docs) ao Claude, VSCode e outros softwares via MCP para obter respostas em tempo real.