import pprint as pp
import os
from utils.log import Log
class PizzaController:
    def __init__(self, driver):
        self.driver = driver[0]

    def db_engine(self, query):
        with self.driver.session() as graphDB_Session:
            nodes = graphDB_Session.run(query)
            # for node in nodes:
            #     pp.pprint(node[0])
            return nodes

    def db_engine_list(self, query):
        nodes = self.db_engine(query)
        for node in nodes:
            pp.pprint(node[0])

    def build_standard_database(self):
        # Using readline()
        cur_path = os.path.dirname(__file__)
        path = cur_path.replace("\\controller", "") + "\\database\\build.cypher"
        
        file = open(path, 'r', encoding='utf-8')
        
        query = ""

        while True:
            line = file.readline()
            query = line.strip()

            if not (query == ""):
                self.db_engine_list(query)

            if not line:
                break

        Log.info("Database construído com sucesso!", "success", "PizzaController")

        file.close()

    def show_all_pizzas(self):

        query = "MATCH (p:Pizza) RETURN p.name"

        self.db_engine_list(query)

        Log.info("Segura essas pizzas!","success","PizzaController")

    def show_all_ingredients(self):

        query = "MATCH (i:Ingredient) RETURN i.name"

        self.db_engine_list(query)

        Log.info("Olha aí esses ingredientes!","success","PizzaController")
    
    def show_pizza_ingredients(self, name):
        query = "MATCH (p:Pizza{name:'{}'})-[:CONTAIN]->(i:Ingredient) RETURN i".format(name)

        self.db_engine_list(query)

    def create_new_pizza(self, name):
        name = input("Insira o nome da Pizza: ")

        print("selecione os ingredientes:")
        while True:
            self.show_all_ingredients()


