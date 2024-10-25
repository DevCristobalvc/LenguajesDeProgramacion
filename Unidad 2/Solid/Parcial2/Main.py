# Punto de entrada para la ejecución de la aplicación.

from Model import *
from View import *
from Controller import *

def main():
    myModel = ProductModel()
    myView = ProductView()
    myController = ProductCatalogController(myModel, myView)
# Se añade while para la interacción del usuario
    while True:
        print("\nMenu\n")
        print("1. Adicionar Producto")
        print("2. Mostrar Catálogo")
        print("3. Cambiar Estrategia de Descuento")
        print("4. Salir\n")

        try:
            sel = int(input("Seleccione una opción: "))
            if sel == 1:
                myController.addNewProduct()
            elif sel == 2:
                myController.showProducts()
            elif sel == 3:
                myController.applyDiscount()
            elif sel == 4:
                break
            else:
                print("Opción no válida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
