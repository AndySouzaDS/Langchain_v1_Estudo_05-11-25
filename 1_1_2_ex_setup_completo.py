# os.environ - em Python é um objeto semelhante a um dicionário que representa as variáveis de ambiente do sistema operacional. 
# Ele permite que você acesse, defina e modifique essas variáveis, que podem conter informações como chaves de API, credenciais de banco de dados e configurações do sistema. 
# É uma ferramenta essencial para interagir com o sistema operacional e configurar aplicativos de forma dinâmica. 

#%%
import os

print('os importado')

#%%
# 1. Acessar variáveis: Use a sintaxe de dicionário para acessar o valor de uma variável. Se a variável não existir, isso gerará um KeyError. 

# 1.1. Obtém o valor da variável de ambiente 'HOME'
home_dir = os.environ['HOME']
print(home_dir)

#%%
# 2. Definir variáveis
# define uma nova variável de ambiente (válida apenas o projeto atual)
os.environ['MINHA_VARIAVEL'] = 'meu_valor'
print(os.environ['MINHA_VARIAVEL'])

#%%
# 3. Remover variáveis
# remove uma variável de ambinte
del os.environ['MINHA_VARIAVEL']


#%%
# 4. Obter variável 
# Usar get() evita erros e acessa uma variável de forma segura, use os.environ.get(). Se a variável não existir, ele retorna None ou um valor padrão que você pode especificar. 

# 4.1. tenta obter a variável; se não existir, retorna None
api_key = os.environ.get('API_KEY')
print(api_key)

#%%
# 4.2. tenta obter a variável; se não existir, retorna o valor padrão especificado
user_id = os.environ.get('USER_ID', 'Variável de ambiente não encontrada!')
print(user_id)


#%%
# 5. Lista Variáveis
# Listar todas as variáveis: Você pode imprimir todas as variáveis de ambiente para ver quais estão disponíveis. 
# Nota: Se o os.environ é um dicionário python, podemos utilizar métodos como o items()
for key, value in os.environ.items():
    print(f'{key}: {value}')


# %%
