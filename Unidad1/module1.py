# module1.py

# Función para agregar un nuevo elemento a una lista
def add_element(list_name, id, name, *args):
    if list_name == 'users':
        new_element = {"id": id, "userName": name, "Country": args[0], "age": args[1]}
    elif list_name == 'videogames':
        new_element = {"id": id, "name": name, "genere": args[0], "title": args[1], "downloads": args[2]}
    elif list_name == 'publishers':
        new_element = {"id": id, "name": name, "country": args[0], "tot_sales": args[1]}
    elif list_name == 'reviews':
        new_element = {"id": id, "name": name, "tot_reviews": args[0]}
    else:
        raise ValueError("Lista no válida")
    
    return new_element

# Función para leer un elemento por ID en una lista
def get_element(list_name, id):
    for element in list_name:
        if element["id"] == id:
            return element
    return None

# Función para actualizar un elemento por ID en una lista
def update_element(list_name, id, **kwargs):
    for element in list_name:
        if element["id"] == id:
            for key, value in kwargs.items():
                if value is not None and key in element:
                    element[key] = value
            return element
    return None

# Función para borrar un elemento por ID en una lista
def delete_element(list_name, id):
    for element in list_name:
        if element["id"] == id:
            list_name.remove(element)
            return True
    return False

# Función para filtrar publishers por valor de ventas totales
def filter_publishers_by_sales(publishers, min_sales, nombre):
    return [publisher for publisher in publishers if publisher["tot_sales"] >= min_sales and publisher["name"] == nombre]
