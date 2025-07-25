# Função para aplicar o desconto
def aplicar_desconto():
    try:
        # Solicitar o preço original do produto
        preco_original = float(input("Digite o preço original do produto (R$): ").strip())

        # Solicitar o percentual de desconto
        desconto_percentual = float(input("Digite o percentual de desconto (%): ").strip())

        # Calcular o valor do desconto
        desconto = (preco_original * desconto_percentual) / 100

        # Calcular o preço final após o desconto
        preco_final = preco_original - desconto

        # Exibir o preço final com duas casas decimais
        print(f"\nPreço original: R$ {preco_original:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Preço final com desconto: R$ {preco_final:.2f}")
    
    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido para o preço e o desconto.")

# Chama a função para aplicar o desconto
aplicar_desconto()
