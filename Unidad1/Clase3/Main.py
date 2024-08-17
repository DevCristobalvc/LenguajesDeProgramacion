from Modulo1 import *

# método "main" del módulo:
if __name__ == "__main__":
    while True:
        print("1. agregar publisher\n")
        print("2. filtrar\n")
        print("3. salir\n")

        op = int(input("ingrese opción deseada:"))

        # crear publishers:
        if op == 1:
            id = input("ingrese el id\n")
            nombre = input("ingrese el nombre\n")
            pais = input("ingrese el pais\n")
            tot_ventas = input("ingrese el total de ventas\n")
            addPublisher(id, nombre, pais, tot_ventas)            
        elif op == 2:
            tot_ventas = input("ingrese el total de ventas\n")
            filtered_publishers = filterPublisherByTotalSales_FilterLambda(tot_ventas)
            if filtered_publishers:
                print("Publishers filtrados:")
                for publisher in filtered_publishers:
                    print(publisher)
            else:
                print("No se encontraron publishers con ese total de ventas.")
        elif op == 3:
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
