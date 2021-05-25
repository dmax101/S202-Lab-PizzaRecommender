from utils.log import Log

import pprint as pp

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
            print("3 - Listar Pizzas por categoria")
            print("4 - Comprar pizzas")
            print("0 - Sair")
            
            op = input("Escolha sua opção: ")

            if op == "1": # Menu Ingredients
                print(50 * "-")
                print("Ingredientes - Opções")
                print(50 * "-")
                print("1 - Adicionar novo Ingrediente")
                print("2 - Apagar Ingrediente")
                print("3 - Editar Ingrediente")
                print("4 - Listar todos os Ingredientes")
                print("5 - Busca de pizzas com os ingredientes")
                print("0 - Voltar")

                op = input("Escolha sua opção: ")
                if op == "1": # Adicionar novo Ingrediente
                    self.pc.create_new_ingredient(input("Insira o nome do novo ingrediente:\n"))
                    input("Pressione enter para continuar...")
                elif op == "2": # Apagar Ingrediente
                    self.pc.show_all_ingredients()
                    ingredient_name = input("Selecione a ingrediente que deseja apagar:\n")
                    
                    self.pc.delete_ingredient(ingredient_name)
                    input("Pressione enter para continuar...")
                elif op == "3": # Editar Ingrediente
                    input("Pressione enter para continuar...")
                    pass
                elif op == "4": # Listar todos os Ingredientes
                    self.pc.show_all_ingredients()
                    input("Pressione enter para continuar...")
                elif op == "5": # Busca de pizzas com os ingredientes
                    input("Pressione enter para continuar...")
                    pass
                elif op == "0": # Voltar
                    pass
            elif op == "2": # Menu Pizzas
                print(50 * "-")
                print("Pizzas - Opções")
                print(50 * "-")
                print("1 - Adicionar nova Pizza")
                print("2 - Apagar Pizza")
                print("3 - Editar Preço Pizza")
                print("4 - Listar todas as Pizza")
                print("5 - Busca os ingredientes da Pizza")
                print("0 - Voltar")

                op = input("Escolha sua opção: ")
                if op == "1": # Adicionar nova Pizza
                    pizza_name = input("Insira o nome da nova Pizza:\n")
                    pizza_price = input("Insira o preço da nova Pizza:\n")
                    pizza_category = input("Insira se é salgada, doce ou vegana:\n")
                    pizza_ingredients = []

                    while True:
                        self.pc.show_all_ingredients()
                        ingredient = input("Adicione os Ingredientes ou 0 para sair:\n")
                        if ingredient == "0" and len(pizza_ingredients) > 1:
                            break
                        elif ingredient == "0" and len(pizza_ingredients) == 0:
                            Log.info("Precisa de no mínimo um ingrediente válido!")
                        elif ingredient == "0": 
                            break
                        else:
                            pizza_ingredients.append(ingredient)

                    self.pc.create_new_pizza(pizza_name, pizza_price, pizza_category, set(pizza_ingredients))
                    input("Pressione enter para continuar...")
                elif op == "2": # Apagar Pizza
                    self.pc.show_all_pizzas()
                    pizza_name = input("Selecione a pizza que deseja apagar:\n")
                    
                    self.pc.delete_pizza(pizza_name)
                    input("Pressione enter para continuar...")
                elif op == "3": # Editar preço da Pizza
                    self.pc.show_all_pizzas()
                    pizza_name = input("Selecione a pizza que deseja editar:\n")
                    new_price = input("Digite o novo valor:\n")

                    self.pc.edit_pizza_price(pizza_name, new_price)
                    input("Pressione enter para continuar...")
                    pass
                elif op == "4": # Listar todas as Pizzas
                    self.pc.show_all_pizzas()
                    input("Pressione enter para continuar...")
                elif op == "5": # Busca os ingredientes da Pizza"
                    self.pc.show_all_pizzas()

                    pizza_name = input("Selecione a pizza para ver os ingredientes:\n")

                    self.pc.show_pizza_ingredients(pizza_name)
                    input("Pressione enter para continuar...")
                elif op == "0": # Voltar
                    pass
            elif op == "3": # Listar Pizzas por categoria
                self.pc.show_all_categories()
                
                self.pc.show_pizzas_from_category(input("Insira o nome da categoria:\n"))
                input("Pressione enter para continuar...")
            elif op == "4": # Comprar pizzas
                pizza_list = []
                pizza_array = []
                
                while True:
                    self.pc.show_all_pizzas()
                    op = input("Digite o nome da pizza ou 0 para concluir a compra:\n")
                    
                    if op == "0":
                        break

                    pizza_list.append(self.pc.locate_pizza(op))

                    print(50 * "-")
                    print("Carrinho de compras")
                    print(50 * "-")

                    total_parcial = 0
                    for pizza in pizza_list:
                        print("{}: R$ {}".format(pizza["name"], pizza["price"]))
                        total_parcial += pizza["price"]
                    print(50 * "-")
                    print("TOTAL PARCIAL DO CARRINHO: R$ {:.2f}".format(total_parcial))
                    print(50 * "-")

                for pizza in pizza_list:
                    pizza_array.append(pizza["name"])

                total_bd = self.pc.calculate_total(pizza_array)

                for pizza in pizza_list:
                        print("{}: R$ {}".format(pizza["name"], pizza["price"]))
                        total_parcial += pizza["price"]
                print(50 * "-")
                print("TOTAL FINAL DO CARRINHO: R$ {:.2f}".format(total_bd))
                print(50 * "-")

                input("Pressione enter para continuar...")
            elif op == "0": # Exit program
                break