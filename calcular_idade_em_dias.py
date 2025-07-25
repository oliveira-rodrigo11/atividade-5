from datetime import datetime

# Função para calcular a idade em dias
def calcular_idade_em_dias():
    try:
        # Solicita o ano de nascimento da pessoa
        ano_nascimento = int(input("Digite o ano de nascimento: ").strip())

        # Obtém o ano atual automaticamente
        ano_atual = datetime.now().year

        # Calcula a idade em anos
        idade_anos = ano_atual - ano_nascimento

        # Calcula a idade em dias (desconsiderando anos bissextos)
        idade_dias = idade_anos * 365

        # Exibe o resultado
        print(f"A idade aproximada de uma pessoa nascida em {ano_nascimento} é de {idade_dias} dias.")
    
    except ValueError:
        print("Erro: Por favor, insira um ano válido.")

# Chama a função para calcular a idade em dias
calcular_idade_em_dias()
