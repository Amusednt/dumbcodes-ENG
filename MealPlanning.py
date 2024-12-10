class PlanoDeRefeicoes:
    def __init__(self):
        self.refeicoes = {
            "Segunda": [],
            "Terça": [],
            "Quarta": [],
            "Quinta": [],
            "Sexta": [],
            "Sábado": [],
            "Domingo": []
        }

    def adicionar_refeicao(self, dia, refeicao):
        if dia in self.refeicoes:
            self.refeicoes[dia].append(refeicao)
            print(f'Refeição "{refeicao}" adicionada ao {dia}.')
        else:
            print("Dia inválido. Por favor, escolha um dia da semana.")

    def remover_refeicao(self, dia, refeicao):
        if dia in self.refeicoes:
            try:
                self.refeicoes[dia].remove(refeicao)
                print(f'Refeição "{refeicao}" removida do {dia}.')
            except ValueError:
                print(f'Refeição "{refeicao}" não encontrada no {dia}.')
        else:
            print("Dia inválido. Por favor, escolha um dia da semana.")

    def visualizar_refeicoes(self):
        for dia, refeicoes in self.refeicoes.items():
            print(f'{dia}: {", ".join(refeicoes) if refeicoes else "Nenhuma refeição planejada."}')

def main():
    plano = PlanoDeRefeicoes()
    
    while True:
        print("\nGerenciador de Planos de Refeições Semanais")
        print("1. Adicionar Refeição")
        print("2. Remover Refeição")
        print("3. Visualizar Refeições")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            dia = input("Digite o dia da semana: ")
            refeicao = input("Digite a refeição a ser adicionada: ")
            plano.adicionar_refeicao(dia, refeicao)
        elif opcao == '2':
            dia = input("Digite o dia da semana: ")
            refeicao = input("Digite a refeição a ser removida: ")
            plano.remover_refeicao(dia, refeicao)
        elif opcao == '3':
            plano.visualizar_refeicoes()
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()