# Ingenieria_en_Mecatronica

# Programa_Sintaxis_y_Semantica_Cuantificadores

from sympy import symbols

def check_universal_quantifier(predicate, domain):
    """Verifica si una afirmación cuantificada universalmente es verdadera para un dominio dado."""
    for element in domain:
        if not predicate.subs({x: element}):  # Evaluamos el predicado para cada elemento del dominio
            return False
    return True

# Definimos las variables simbólicas
x = symbols('x')

# Definimos una expresión que queremos verificar
# Por ejemplo, queremos verificar si para todo x en el dominio de los enteros, x + 1 es mayor que x
predicate = x + 1 > x

# Definimos el dominio de los enteros
integer_domain = range(-10, 11)  # Seleccionamos un rango de -10 a 10 como dominio

# Verificamos si la afirmación es verdadera para el dominio de los enteros
result = check_universal_quantifier(predicate, integer_domain)

# Imprimimos el resultado
print("¿La afirmación es verdadera para todo x en el dominio de los enteros?", result)
