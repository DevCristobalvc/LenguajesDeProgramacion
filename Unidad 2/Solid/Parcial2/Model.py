# Aquí se maneja la lógica del modelo de productos y el patrón Observer.
# Notifica cuando se agrega, imorimiendo en la interfaz de usuario
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class ProductModel:
    def __init__(self):
        self.catalog = []
        self.observers = []

    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.catalog)

    def addProduct(self, product: Product):
        self.catalog.append(product)
        self.notifyObservers()

    def getCatalog(self):
        return self.catalog
