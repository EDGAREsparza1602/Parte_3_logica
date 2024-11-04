from sympy import symbols, Or, And, Not, to_cnf, satisfiable

# Definir los símbolos para las variables
x, y, z = symbols('x y z')

# Definir la fórmula lógica de ejemplo
formula = Or(And(x, y), And(Not(x), z))

# Mostrar la fórmula original
print("Fórmula original:", formula)

# Convertir la fórmula a CNF (Forma Normal Conjuntiva)
clausulas_horn = to_cnf(formula)

# Mostrar las cláusulas en CNF
print("Cláusulas en CNF:", clausulas_horn)

# Verificar si la fórmula es satisfacible
satisfacible = satisfiable(clausulas_horn)

# Imprimir el resultado
if satisfacible:
    print("La fórmula es satisfacible.")
else:
    print("La fórmula no es satisfacible.")
