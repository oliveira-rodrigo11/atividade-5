import re  # Para utilizar expressões regulares

# Função para verificar se uma palavra ou frase é um palíndromo
def verificar_palindromo():
    # Solicita a entrada do usuário
    frase = input("Digite uma palavra ou frase para verificar se é um palíndromo: ").strip()

    # Remove espaços, pontuação e converte para minúsculas
    frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()

    # Verifica se a frase limpa é igual à sua inversa
    if frase_limpa == frase_limpa[::-1]:
        print("Sim")
    else:
        print("Não")

# Chama a função para verificar o palíndromo
verificar_palindromo()
