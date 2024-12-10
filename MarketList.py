class ListaDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f'Item "{item}" adicionado à lista de compras.')

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f'Item "{item}" removido da lista de compras.')
        else:
            print(f'Item "{item}" não encontrado na lista.')

    def editar_item(self, item_antigo, item_novo):
        if item_antigo in self.itens:
            index = self.itens.index(item_antigo)
            self.itens[index] = item_novo
            print(f'Item "{item_antigo}" editado para "{item_novo}".')
        else:
            print(f'Item "{item_antigo}" não encontrado na lista.')

    def visualizar_itens(self):
        if self.itens:
            print("Lista de Compras:")
            for item in self.itens:
                print(f'- {item}')
        else:
            print("A lista de compras está vazia.")

def main():
    lista = ListaDeCompras()

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Editar item")
        print("4. Visualizar itens")
        print("5. Sair")

        opcao = input("Digite o número da opção: ")

        if opcao == '1':
            item = input("Digite o nome do item a ser adicionado: ")
            lista.adicionar_item(item)
        elif opcao == '2':
            item = input("Digite o nome do item a ser removido: ")
            lista.remover_item(item)
        elif opcao == '3':
            item_antigo = input("Digite o nome do item a ser editado: ")
            item_novo = input("Digite o novo nome do item: ")
            lista.editar_item(item_antigo, item_novo)
        elif opcao == '4':
            lista.visualizar_itens()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()