from model.connector import Connector
from controller.pizza_controller import PizzaController
from utils.log import Log
from view.menu import Menu
import sys

conf = {
        "host": "localhost",
        "port": 7689,
        "user": "neo4j",
        "password": "toor"
    }

def setup():
    if input('Deseja utilizar as configurações de conexão padrão?\n(s|n): ') == 'n':
        conf["host"] = input('Host\n> ')
        conf["port"] = input('Porta\n> ')
        conf["user"] = input('Usuário\n> ')
        conf["password"] = input('Senha\n> ')
    else:
        ('Usando configurações padrão.')

    if input('\nDeseja reconstruir o banco de dados?\n!!! Isto irá eliminar todos os dados preexistentes !!!\n(s|n): ') == 's':
        cn = Connector(
            conf["host"],
            conf["port"],
            conf["user"],
            conf["password"]
        )

        cn.connect()

        pc = PizzaController([cn.driver])
        pc.build_standard_database()

        cn.close()
    else:
        Log.info('Base de dados inalterada.', "success")

def main():
    cn = Connector(
        conf["host"],
        conf["port"],
        conf["user"],
        conf["password"]
    )

    cn.connect()

    pc = PizzaController([cn.driver])

    menu = Menu([pc])

    menu.show_display()

    #pc.show_all_pizza()

    cn.close()

if __name__ == '__main__':
    for arg in sys.argv:
        if arg == "setup":
            setup()
    main()