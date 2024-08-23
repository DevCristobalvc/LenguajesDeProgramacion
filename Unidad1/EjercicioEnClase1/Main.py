from functools import reduce

# Lista de secuencias de ADN
secuencias_adn = [
    "ATCGATCGA", 
    "GGTACGTA", 
    "CAGTTGCA", 
    "GCGCGCGCGC", 
    "AATTCCGG", 
    "TTAAACCGG", 
    "GGATCGATCG"
]

# Función para calcular el porcentaje de 'A' en una secuencia
def porcentaje_a(secuencia):
    return (secuencia.count('A') / len(secuencia)) * 100

# Aplicar la función para obtener el porcentaje de 'A' en cada secuencia
porcentajes_a = list(map(porcentaje_a, secuencias_adn))

# Filtrar las secuencias con porcentaje mayor a 25%
secuencias_filtradas = list(filter(lambda sec: porcentaje_a(sec) > 25, secuencias_adn))

# Concatenar las secuencias filtradas
secuencia_concatenada = reduce(lambda x, y: x + y, secuencias_filtradas)

# Calcular la longitud total de la secuencia concatenada
longitud_total = len(secuencia_concatenada)

# Resultados
print("Secuencias filtradas:", secuencias_filtradas)
print("Secuencia concatenada:", secuencia_concatenada)
print("Longitud total:", longitud_total)
