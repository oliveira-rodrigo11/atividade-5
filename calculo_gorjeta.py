# Função para calcular a gorjeta
def calcular_gorjeta():
    try:
        # Definindo o valor da conta
        valor_conta = 100.00  # Exemplo de valor da conta

        # Solicitar ao usuário a porcentagem da gorjeta
        porcentagem = float(input("Informe a porcentagem da gorjeta (ex: 10, 15, 20): ").strip())

        # Calcular o valor da gorjeta
        valor_gorjeta = (valor_conta * porcentagem) / 100

        # Exibir o valor da gorjeta com 2 casas decimais
        print(f"\nValor da conta: R$ {valor_conta:.2f}")
        print(f"Porcentagem da gorjeta: {porcentagem}%")
        print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
    
    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido para a porcentagem.")

# Chama a função para calcular a gorjeta
calcular_gorjeta()
