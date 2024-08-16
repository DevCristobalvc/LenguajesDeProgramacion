# main.py

from module1 import add_element, filter_publishers_by_sales

# Listas para almacenar datos
users = []         # Lista para almacenar los usuarios
publishers = []    # Lista para almacenar los editores
videogames = []    # Lista para almacenar los videojuegos
reviews = []       # Lista para almacenar las reseñas

# Función para agregar un nuevo publisher
def add_publisher():
    try:
        id = int(input("Ingrese el ID del publisher: "))
        name = input("Ingrese el nombre del publisher: ")
        country = input("Ingrese el país del publisher: ")
        tot_sales = float(input("Ingrese el total de ventas del publisher: "))
        new_publisher = add_element('publishers', id, name, country, tot_sales)
        publishers.append(new_publisher)
        print("Publisher agregado exitosamente.")
    except ValueError as e:
        print(f"Error: {e}")

# Función para mostrar todos los publishers
def show_publishers(publishers_list):
    for publisher in publishers_list:
        print(publisher)

# Función principal para ejecutar el programa
def main():
    while True:
        print("\n1. Agregar Publisher")
        print("2. Filtrar Publishers por ventas totales")
        print("3. Mostrar Publishers")
        print("4. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            add_publisher()
        elif choice == '2':
            try:
                min_sales = float(input("Ingrese el valor mínimo de ventas: "))
                nombre = str(input("Ingresa el nombre: "))
                filtered_publishers = filter_publishers_by_sales(publishers, min_sales, nombre)
                print("\nPublishers filtrados:")
                show_publishers(filtered_publishers)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '3':
            print("\nTodos los Publishers:")
            show_publishers(publishers)
        elif choice == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
