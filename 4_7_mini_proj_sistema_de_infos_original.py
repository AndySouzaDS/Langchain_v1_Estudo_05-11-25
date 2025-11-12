# 🚀 MINI-PROJETO 1: Sistema de Informações

# **Objetivo:** Integrar tudo que aprendeu até agora

# Crie um sistema com:

# 1. 3 tools customizadas (você escolhe o tema)
# 2. Uma função que lista todas as tools disponíveis
# 3. Um menu interativo que permite testar cada tool 
# ----------------------------------------------------------
#%%
from langchain_core.tools import tool

#%%
# 1. 3 tools customizadas (você escolhe o tema)
@tool
def info_pais(pais: str) -> str:
    """Retorna informações básicas sobre um país."""
    paises = {
        "brasil": "Capital: Brasília, População: 214M, Idioma: Português",
        "eua": "Capital: Washington DC, População: 350M, Idioma: Inglês",
        "japao": "Capital: Tóquio, População: 125M, Idioma: Japonês"
    }
    return paises.get(pais.lower(), "País não encontrado no banco de dados")

@tool
def calcular_idade(ano_nascimento: int) -> str:
    """Calcula a idade baseada no ano de nascimento."""
    from datetime import datetime
    idade = datetime.now().year


#%%
from datetime import datetime

idade = datetime.now()
print(idade)

# %%
