def calcular_imposto(renda):
    if renda <= 22847.76:
        return 0.0  # Isento
    elif renda <= 33919.80:
        return (renda - 22847.76) * 0.075  # 7.5%
    elif renda <= 45012.60:
        return (renda - 33919.80) * 0.15 + 825.14  # 15%
    elif renda <= 55976.16:
        return (renda - 45012.60) * 0.225 + 1_440.34  # 22.5%
    else:
        return (renda - 55976.16) * 0.275 + 2_590.58  # 27.5%

def main():
    try:
        renda_anual = float(input("Digite sua renda anual: R$ "))
        imposto = calcular_imposto(renda_anual)
        print(f"O imposto a ser pago é: R$ {imposto:.2f}")
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

if __name__ == "__main__":
    main()