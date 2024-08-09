# Listas para almacenar datos
users = []         # Lista para almacenar los usuarios
publishers = []    # Lista para almacenar los editores
videogames = []    # Lista para almacenar los videojuegos
reviews = []       # Lista para almacenar las reseñas

# Función para agregar un nuevo elemento a una lista
def addElement(list_name, id, name, *args):
    if list_name == users:
        newElement = {"id": id, "userName": name, "Country": args[0], "age": args[1]}
    elif list_name == videogames:
        newElement = {"id": id, "name": name, "genere": args[0], "title": args[1], "downloads": args[2]}
    elif list_name == publishers:
        newElement = {"id": id, "name": name, "country": args[0], "tot_sales": args[1]}
    else:
        raise ValueError("Lista no válida")
    
    list_name.append(newElement)

# Función para leer un elemento por ID en una lista
def getElement(list_name, id):
    for element in list_name:
        if element["id"] == id:
            return element
    return None

# Función para actualizar un elemento por ID en una lista
def updateElement(list_name, id, **kwargs):
    for element in list_name:
        if element["id"] == id:
            for key, value in kwargs.items():
                if value is not None and key in element:
                    element[key] = value
            return element
    return None

# Función para borrar un elemento por ID en una lista
def deleteElement(list_name, id):
    for element in list_name:
        if element["id"] == id:
            list_name.remove(element)
            return True
    return False

# Agregar datos de ejemplo para usuarios
addElement(users, 1, "JohnDoe", "USA", 25)
addElement(users, 2, "JaneDoe", "UK", 30)
addElement(users, 3, "AliceSmith", "Canada", 28)
addElement(users, 4, "BobJohnson", "Australia", 35)

# Agregar datos de ejemplo para videojuegos
addElement(videogames, 1, "EpicQuest", "RPG", "Epic Quest - The Beginning", 150000)
addElement(videogames, 2, "SpaceWarrior", "Shooter", "Space Warrior X", 200000)
addElement(videogames, 3, "PuzzleMaster", "Puzzle", "Puzzle Master Deluxe", 50000)
addElement(videogames, 4, "AdventureLand", "Adventure", "Adventure Land Saga", 120000)

# Agregar datos de ejemplo para editores
addElement(publishers, 1, "GamerWorks", "USA", 5000000)
addElement(publishers, 2, "GameForge", "Germany", 3000000)
addElement(publishers, 3, "PlayRealm", "Japan", 4500000)
addElement(publishers, 4, "NextGenGames", "South Korea", 6000000)

# Imprimir listas para verificar los datos
print("Usuarios:")
print(users)

print("\nVideojuegos:")
print(videogames)

print("\nEditores:")
print(publishers)
