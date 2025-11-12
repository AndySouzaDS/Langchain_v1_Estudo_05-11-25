Perfeito 👏 — você já está **quase certo**!
O seu código segue **exatamente o padrão do LangChain v1.0**.
E sim — dá pra chamar a *tool* diretamente **sem usar agente algum**, do jeito que você fez.

Mas vamos revisar com clareza os **dois jeitos corretos** de chamar uma `@tool` sem agente, para que fique 100% consistente com o comportamento esperado pelo `langchain_core`.

---

## ✅ Opção 1 — usando `.invoke()` (forma recomendada no LangChain v1.0)

```python
#%%
from langchain_core.tools import tool

#%%
@tool
def info_pais(pais: str) -> str:
    """Retorna informações básicas sobre um país."""
    paises = {
        "brasil": "Capital: Brasília, População: 214M, Idioma: Português",
        "eua": "Capital: Washington DC, População: 350M, Idioma: Inglês",
        "japao": "Capital: Tóquio, População: 125M, Idioma: Japonês"
    }
    return paises.get(pais.lower(), "País não encontrado no banco de dados")

#%%
if __name__ == "__main__":
    response = info_pais.invoke({"pais": "Brasil"})
    print(response)
```

🟢 **Explicação:**

* `.invoke()` é a interface **padrão universal do LangChain Core**.
* O argumento deve ser um dicionário (`dict`) com os nomes dos parâmetros da função.

---

## ✅ Opção 2 — chamando diretamente como função Python

Como o `@tool` apenas “envolve” sua função original, você também pode chamá-la como função pura:

```python
if __name__ == "__main__":
    response = info_pais.run("Brasil")
    print(response)
```

ou simplesmente:

```python
if __name__ == "__main__":
    response = info_pais.func("Brasil")  # acessa a função original
    print(response)
```

🟡 **Diferença entre os três métodos:**

| Método                        | Uso                          | Retorno |
| ----------------------------- | ---------------------------- | ------- |
| `.invoke({"pais": "Brasil"})` | Interface LangChain moderna  | string  |
| `.run("Brasil")`              | Interface simplificada       | string  |
| `.func("Brasil")`             | Executa a função Python pura | string  |

---

### 💡 Dica prática

Se você pretende **testar suas Tools manualmente** fora de um agente, use `.invoke()`.
Se quiser **reutilizá-las em um script Python normal**, `.func()` é mais direto.

---

Quer que eu te mostre o mesmo exemplo com **três tools diferentes** sendo chamadas no mesmo script (sem agente), simulando um mini conjunto de ferramentas autônomas?
