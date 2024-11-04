import numpy as np

# Definimos una función para calcular la utilidad esperada de una acción
def utilidad_esperada(probabilidades, utilidades):
    return np.dot(probabilidades, utilidades)

# Definimos las probabilidades y utilidades de cada acción
probabilidades = np.array([0.3, 0.5, 0.2])  # Probabilidades de los resultados
utilidades = np.array([100, 50, 0])          # Utilidades correspondientes

# Calculamos la utilidad esperada de la acción
utilidad_esperada_accion = utilidad_esperada(probabilidades, utilidades)

# Imprimimos la utilidad esperada
print(f"Utilidad esperada de la acción: {utilidad_esperada_accion}")

# Dado que solo hay una acción en este contexto, seleccionamos la acción
print("La mejor acción es la única acción disponible.")
