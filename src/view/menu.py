from utils.log import Log

class Menu:
    def __init__(self, pc):
        self.pc = pc[0]

    def show_display(self):
        while True:
            print(50 * "-")
            print("Olá! Seja bem vindo!")
            print(50 * "-")
            print("1 - Ingredientes")
            print("2 - Pizzas")
            print("0 - Sair")
            
            op = input("Escolha sua opção: ")

            if op == "0":
                break
            elif op == "1":
                print(50 * "-")
                print("Ingredientes - Opções")
                print(50 * "-")
                print("1 - Adicionar novo Ingrediente")
                print("2 - Apagar Ingrediente")
                print("3 - Editar Ingrediente")
                print("4 - Listar todos os Ingredients")
                print("0 - Voltar")

                op = input("Escolha sua opção: ")
                if op == "1":
                    # Adicionar novo Ingrediente
                    pass
                elif op == "2":
                    # Apagar Ingrediente
                    pass
                elif op == "3":
                    # Editar Ingrediente
                    pass
                elif op == "4":
                    self.pc.show_all_ingredients()
                elif op == "0":
                    break
                







            
            print("2 - Adicionar nova Pizza")
            print("3 - Buscar Pizza")
            print("4 - Editar Pizza")
            print("6 - Apagar Pizza")
