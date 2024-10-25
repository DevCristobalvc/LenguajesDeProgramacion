# imprime la interfaz de usuario y se encarga de la interacción con el usuario.

class ProductView:
    def displayCatalog(self, products):
        if products:
            print("\nLista de productos")
            for name, price, category in products:
                print(f"Producto: {name}, Precio: {price:.2f}, Categoría: {category}")
        else:
            print("El catálogo está vacío")

    def addNewProduct(self):
        name = input("\nIngrese el nombre del nuevo producto: ")
        price = float(input("Ingrese el precio del nuevo producto: "))
        category = input("Ingrese la categoría del nuevo producto: ")
        return name, price, category

    def update(self, catalog):
        print("\nEl catálogo ha sido actualizado:")
        discounted_catalog = [(p.name, p.price, p.category) for p in catalog]  # Aquí no aplicamos descuento
        self.displayCatalog(discounted_catalog)

