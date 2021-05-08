import pprint as pp

class PizzaController:
    def __init__(self, driver):
        self.driver = driver[0]

    def show_all_pizza(self):
        with self.driver.session() as graphDB_Session:
            nodes = graphDB_Session.run("MATCH (p:Pizza) RETURN p.name")
            for node in nodes:
                pp.pprint(node[0])
                #print(node[0])