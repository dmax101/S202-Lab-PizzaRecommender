from model.connector import Connector
from controller.pizza_controller import PizzaController

def main():
    conf = {
        "host": "localhost",
        "port": 7689,
        "user": "neo4j",
        "password": "toor"
    }

    cn = Connector(
        conf["host"],
        conf["port"],
        conf["user"],
        conf["password"]
    )

    cn.connect()

    pc = PizzaController([cn.driver])

    pc.show_all_pizza()

    cn.close()

if __name__ == '__main__':
    main()