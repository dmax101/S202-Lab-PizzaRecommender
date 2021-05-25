import pprint as pp
import os
from utils.log import Log
class PizzaController:
    def __init__(self, driver):
        self.driver = driver[0]

    def db_engine(self, query, list=False):
        with self.driver.session() as graphDB_Session:
            nodes = graphDB_Session.run(query)
        
            if list == True:
                for node in nodes:
                    if len(node) == 1:
                        name = "{}".format(node[0])
                        print(name)
                    else:
                        name = "{}".format(node[0])
                        price = "{}".format(node[1])
                        print(name + ": R$ " + price)
            else:
                for node in nodes:
                    if "SUM(p.price)" in node.data():
                        sum_node = float(node["SUM(p.price)"])
                        return sum_node
                    
                    if len(node['p']) == 1:
                        name = node['p']['name']
                        return [name]
                    else:
                        name = node['p']['name']
                        price = float(node['p']['price'])
                        
                        return {"name": name, "price": price}

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
                self.db_engine(query, True)

            if not line:
                break

        Log.info("Database construído com sucesso!", "success", "PizzaController")

        file.close()

    def show_all_categories(self):

        query = "MATCH (c:Category) RETURN c.name"

        self.db_engine(query, True)

        Log.info("Segura essas pizzas!","success","PizzaController")

    def show_all_pizzas(self):

        query = "MATCH (p:Pizza) RETURN p.name, p.price"

        self.db_engine(query, True)

        Log.info("Segura essas pizzas!","success","PizzaController")

    def show_all_ingredients(self):

        query = "MATCH (i:Ingredient) RETURN i.name"

        self.db_engine(query, True)

        Log.info("Olha aí esses ingredientes!","success","PizzaController")
    
    def show_pizzas_from_category(self, name):
        query = "MATCH (n:Category{name: '" + name + "'})-[:HAS]->(p:Pizza) RETURN p.name"

        self.db_engine(query, True)

    def show_pizza_ingredients(self, name):
        query = "MATCH (p:Pizza{name:'{" + name + "}'})-[:CONTAIN]->(i:Ingredient) RETURN i"

        self.db_engine(query, True)

    def show_ingredients_pizza(self, name):
        query = "MATCH (i:Ingredient{name:'{" + name + "}'})<-[:CONTAIN]-(p:Pizza) RETURN p"

        self.db_engine(query, True)

    def create_new_ingredient(self, name):
        query = "MERGE (i:Ingredient{name: '" + name + "'})"
        Log.info(str(query), "warning", "PizzaController")

        self.db_engine(query)

    def create_new_pizza(self, name, price, category, ingredients):
        query = "MERGE (p:Pizza{name: '" + name + "', price: " + price + "})"

        self.db_engine(query)

        query = "MATCH (p:Pizza{name: '" + name + "'}), (c:Category{name: '" + category + "'}) CREATE (c)-[:HAS]->(p)"

        self.db_engine(query)
        
        for ingredient in ingredients:
            self.db_engine("MERGE (i:Ingredient{name: '" + ingredient + "'})")
            self.db_engine("MATCH (p:Pizza{name: '" + name + "'}), (i:Ingredient{name: '" + ingredient + "'}) CREATE (p)-[:CONTAIN]->(i)")

    def locate_pizza(self, name):
        query = "MATCH (p:Pizza{name: '" + name + "'}) RETURN p"

        response = self.db_engine(query)
        
        print(response)
        
        return response

    def locate_ingredient(self, name):
        query = "MATCH (i:Ingredient{name: '" + name + "'}) RETURN i"

        response = self.db_engine(query)
        
        print(response)
        
        return response

    def delete_ingredient(self, name):
        query = "MATCH (i:Ingredient{name: '" + name + "'}) DETACH DELETE i"

        self.db_engine(query)

    def delete_pizza(self, name):
        query = "MATCH (p:Pizza{name: '" + name + "'}) DETACH DELETE p"

        self.db_engine(query)

    def calculate_total(self, pizzas):
        query = "MATCH (p:Pizza) WHERE p.name IN {} RETURN SUM(p.price)".format(pizzas)

        return self.db_engine(query)

    def edit_pizza_price(self, name, price):
        query = "MATCH (p:Pizza{name: '" + name + "'}) SET p.price = " + price

        self.db_engine(query)
        