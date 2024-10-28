# Conversor de Unidades

def converter_temperatura(valor, de_unidade, para_unidade):
    """Converte temperaturas entre Celsius, Fahrenheit e Kelvin."""
    if de_unidade == 'C':
        if para_unidade == 'F':
            return valor * 9/5 + 32  # Celsius para Fahrenheit
        elif para_unidade == 'K':
            return valor + 273.15  # Celsius para Kelvin
    elif de_unidade == 'F':
        if para_unidade == 'C':
            return (valor - 32) * 5/9  # Fahrenheit para Celsius
        elif para_unidade == 'K':
            return (valor - 32) * 5/9 + 273.15  # Fahrenheit para Kelvin
    elif de_unidade == 'K':
        if para_unidade == 'C':
            return valor - 273.15  # Kelvin para Celsius
        elif para_unidade == 'F':
            return (valor - 273.15) * 9/5 + 32  # Kelvin para Fahrenheit
    return None

def converter_comprimento(valor, de_unidade, para_unidade):
    """Converte comprimentos entre metros, quilômetros e milhas."""
    if de_unidade == 'm':
        if para_unidade == 'km':
            return valor / 1000  # Metros para Quilômetros
        elif para_unidade == 'mi':
            return valor / 1609.34  # Metros para Milhas
    elif de_unidade == 'km':
        if para_unidade == 'm':
            return valor * 1000  # Quilômetros para Metros
        elif para_unidade == 'mi':
            return valor / 1.60934  # Quilômetros para Milhas
    elif de_unidade == 'mi':
        if para_unidade == 'm':
            return valor * 1609.34  # Milhas para Metros
        elif para_unidade == 'km':
            return valor * 1.60934  # Milhas para Quilômetros
    return None

def converter_massa(valor, de_unidade, para_unidade):
    """Converte massas entre gramas, quilogramas e libras."""
    if de_unidade == 'g':
        if para_unidade == 'kg':
            return valor / 1000  # Gramas para Quilogramas
        elif para_unidade == 'lb':
            return valor / 453.592  # Gramas para Libras
    elif de_unidade == 'kg':
        if para_unidade == 'g':
            return valor * 1000  # Quilogramas para Gramas
        elif para_unidade == 'lb':
            return valor * 2.20462  # Quilogramas para Libras
    elif de_unidade == 'lb':
        if para_unidade == 'g':
            return valor * 453.592  # Libras para Gramas
        elif para_unidade == 'kg':
            return valor / 2.20462  # Libras para Quilogramas
    return None

def main():
    print("Conversor de Unidades")
    print("1. Temperatura")
    print("2. Comprimento")
    print("3. Massa")
    
    escolha = input("Escolha o tipo de conversão (1/2/3): ")
    
    if escolha == '1':
        valor = float(input("Digite o valor da temperatura: "))
        de_unidade = input("Digite a unidade de origem (C/F/K): ").upper()
        para_unidade = input("Digite a unidade de destino (C/F/K): ").upper()
        resultado = converter_temperatura(valor, de_unidade, para_unidade)
    
    elif escolha == '2':
        valor = float(input("Digite o valor do comprimento: "))
        de_unidade = input("Digite a unidade de origem (m/km/mi): ").lower()
        para_unidade = input("Digite a unidade de destino (m/km/mi): ").lower()
        resultado = converter_comprimento(valor, de_unidade, para_unidade)
    
    elif escolha == '3':
        valor = float(input("Digite o valor da massa: "))
        de_unidade = input("Digite a unidade de origem (g/kg/lb): ").lower()
        para_unidade = input("Digite a unidade de destino (g/kg/lb): ").lower()
        resultado = converter_massa(valor, de_unidade, para_unidade)
    
    else:
        print("Escolha inválida!")
        return
    
    if resultado is not None:
        print(f"{valor} {de_unidade} é igual a {resultado} {para_unidade}")
    else:
        print("Erro na conversão!")

if __name__ == "__main__":
    main()