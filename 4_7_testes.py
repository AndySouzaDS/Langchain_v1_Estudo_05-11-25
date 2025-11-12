# 3. calcula descontos de preços de produtos

#%%
from langchain_core.tools import tool

@tool
def calcular_desconto(preco_produto: float, valor_desconto: float) -> tuple:
    """
    Calcula o valor do desconto em reais e o preço final do produto.
    O valor do desconto deve ser digitado como número inteiro (ex: 10 para 10%).
    Retorna (valor_desconto_reais, preco_final_produto).
    """
    try:
        if preco_produto <= 0:
            return "Erro: o preço do produto deve ser maior que R$ 0,00."

        if valor_desconto < 0:
            return "Erro: o valor do desconto não pode ser negativo."

        # Se o desconto for 0, o preço não muda
        if valor_desconto == 0:
            return 0.0, round(preco_produto, 2)

        # Converter para fração (ex: 10 → 0.10)
        desconto_frac = valor_desconto / 100

        # Garantir que não ultrapasse 100%
        if desconto_frac > 1:
            return "Erro: o desconto não pode ser maior que 100%."

        valor_desconto_reais = preco_produto * desconto_frac
        preco_final_produto = preco_produto - valor_desconto_reais

        return round(valor_desconto_reais, 2), round(preco_final_produto, 2)

    except Exception as e:
        return f"Erro ao calcular desconto: {e}"

#%%
# Exemplo de uso direto (fora do fluxo de agente)
if __name__ == "__main__":
    preco = float(input("Digite o preço do produto (R$): "))
    desconto = float(input("Digite o valor de desconto (%) (ex: 10 para 10%): "))

    response = calcular_desconto.invoke({"preco_produto": preco, "valor_desconto": desconto})

    if isinstance(response, tuple):
        valor_desc, preco_final = response
        print(f"\n💰 Desconto: R$ {valor_desc:.2f}")
        print(f"💵 Preço final: R$ {preco_final:.2f}")
    else:
        print(f"\n{response}")

# %%
