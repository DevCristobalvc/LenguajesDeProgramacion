# Se ajusta de manera que contiene tanto la lógica del controlador como las estrategias de descuento
# Permite que la vista se actualice automáticamente
from Model import *
from View import *
from abc import ABC, abstractmethod

# Estrategias de Descuento
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, price: float) -> float:
        return price * (1 - self.percentage / 100)

class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply_discount(self, price: float) -> float:
        return max(0, price - self.amount)

class ProductCatalogController:
    def __init__(self, model: ProductModel, view: ProductView):
        self.model = model
        self.view = view
        self.model.addObserver(self.view)
        self.discount_strategy = NoDiscount()  # Estrategia por defecto

    def set_discount_strategy(self, strategy: DiscountStrategy):
        """Método para establecer la estrategia de descuento."""
        self.discount_strategy = strategy

    def addNewProduct(self):
        name, price, category = self.view.addNewProduct()
        self.model.addProduct(Product(name, price, category))

    def showProducts(self):
        catalog = self.model.getCatalog()
        # Prepara el catálogo con descuentos aplicados
        discounted_catalog = [(p.name, self.discount_strategy.apply_discount(p.price), p.category) for p in catalog]
        self.view.displayCatalog(discounted_catalog)

    def applyDiscount(self):
        """Método para aplicar un descuento específico."""
        print("\nOpciones de Descuento:\n")
        print("1. Sin Descuento")
        print("2. Descuento del 20%")
        print("3. Descuento fijo de $5")
        choice = int(input("Seleccione una opción: "))
        
        if choice == 1:
            self.set_discount_strategy(NoDiscount())
        elif choice == 2:
            self.set_discount_strategy(PercentageDiscount(20))
        elif choice == 3:
            self.set_discount_strategy(FixedAmountDiscount(5))
        else:
            print("Opción no válida. Se aplicará sin descuento.")
