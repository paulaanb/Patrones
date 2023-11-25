from directorpizza import PizzaDirector
from pizzapersonalizada import PizzaCustomizadaBuilder
from validar import PizzaValidator
from crearcsv import PizzaCSV

if __name__ == "__main__":
    director = PizzaDirector()
    director.builder = PizzaCustomizadaBuilder()
    csv_writer = PizzaCSV("pizzas.csv")  

    while True:
        director.crear_pizza()
        pizza = director.get_pizza()

        validator = PizzaValidator(director.builder)
        validator.set_pizza(pizza)

        while True:
            if validator.verificar_pizza():
                
                csv_writer.write_pizza_to_csv(pizza)
                break 
        break 
