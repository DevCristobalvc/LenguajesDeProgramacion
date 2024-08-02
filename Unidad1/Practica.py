#Listas
users = []
publishers = []
videogames = []

# Add user
def addUser (id, userName, Country, age):
    newUser = {"id": id,"userName": userName,"Country": Country, "age":age}
    users.append (newUser)


# Add video game
def addViegame (id, name, genere, title,  downloads):
    newUser = {"id": id, "name": name, "genere": genere, "title":title, "downloads": downloads}
    users.append (newUser)

# Add publisher
def addPublishers (id, name, country, tot_sales):
    newPublishers = {"id": id,"name": name,"country": country, "tot_sales": tot_sales}
    publishers.append (newPublishers)


# Add data
addUser(1, )
