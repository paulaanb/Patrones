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
                # Escribe la fila de datos en el archivo CSV
                csv_writer.write_pizza_to_csv(pizza)
                break  # Sal del bucle interno después de confirmar

        break  # Sal del bucle principal después de confirmar
