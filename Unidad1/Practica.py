#Listas
users = []
publishers = []
videogames = []

# CRUD user

# Add user
# Lista de usuarios para almacenar los datos
users = []

# Función para agregar un usuario
def addUser(id, userName, Country, age):
    newUser = {"id": id, "userName": userName, "Country": Country, "age": age}
    users.append(newUser)

# Función para leer un usuario por ID
def getUser(id):
    for user in users:
        if user["id"] == id:
            return user
    return None

# Función para actualizar un usuario por ID
def updateUser(id, newUserName=None, newCountry=None, newAge=None):
    for user in users:
        if user["id"] == id:
            if newUserName is not None:
                user["userName"] = newUserName
            if newCountry is not None:
                user["Country"] = newCountry
            if newAge is not None:
                user["age"] = newAge
            return user
    return None

# Función para borrar un usuario por ID
def deleteUser(id):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return True
    return False

# Ejemplos de uso
addUser(1, "JohnDoe", "USA", 25)
addUser(2, "JaneDoe", "UK", 30)

print(getUser(1))  # Leer usuario con ID 1
updateUser(1, newUserName="JohnnyDoe")  # Actualizar nombre de usuario con ID 1
print(getUser(1))  # Leer usuario con ID 1 después de la actualización
deleteUser(2)  # Borrar usuario con ID 2
print(users)  # Mostrar todos los usuarios restantes

# Add video game
def addViegame (id, name, genere, title,  downloads):
    newUser = {"id": id, "name": name, "genere": genere, "title":title, "downloads": downloads}
    users.append (newUser)

# Add publisher
def addPublishers (id, name, country, tot_sales):
    newPublishers = {"id": id,"name": name,"country": country, "tot_sales": tot_sales}
    publishers.append (newPublishers)

# Delete

# Add data
addUser(1, "cristobal", "colombia", 21)
addUser(1, "cristobal", "colombia", 21)

# Imprimir
print(users)
