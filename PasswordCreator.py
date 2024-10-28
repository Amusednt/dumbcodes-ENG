import random
import string

def gerar_senha(tamanho, complexidade):
    """
    Gera uma senha aleatória com o tamanho e complexidade especificados.

    Args:
        tamanho (int): Tamanho da senha.
        complexidade (str): Nível de complexidade da senha. Pode ser:
            - 'baixa': letras minúsculas
            - 'média': letras minúsculas e maiúsculas
            - 'alta': letras minúsculas, maiúsculas e números
            - 'muito alta': letras minúsculas, maiúsculas, números e caracteres especiais

    Returns:
        str: Senha gerada.
    """
    # Define os caracteres possíveis para cada nível de complexidade
    if complexidade == 'baixa':
        caracteres = string.ascii_lowercase
    elif complexidade == 'média':
        caracteres = string.ascii_letters
    elif complexidade == 'alta':
        caracteres = string.ascii_letters + string.digits
    elif complexidade == 'muito alta':
        caracteres = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Complexidade inválida")

    # Gera a senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

    return senha

# Exemplos de uso
print("Senha com complexidade baixa:", gerar_senha(10, 'baixa'))
print("Senha com complexidade média:", gerar_senha(12, 'média'))
print("Senha com complexidade alta:", gerar_senha(14, 'alta'))
print("Senha com complexidade muito alta:", gerar_senha(16, 'muito alta'))